import datetime
import logging
import os
import pickle

from django.shortcuts import get_object_or_404
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build

import rental.models.booking as m_booking
import rental.models.place as m_place
from rental.models.guest import Guest
from villafleurie.settings import BASE_DIR


def build_service():
    """
    Build Google Calendar API service and returns calendar list and service
    """

    creds = None

    SCOPES = [
        'https://www.googleapis.com/auth/calendar',
        'https://www.googleapis.com/auth/calendar.events'
    ]

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            SECRETS = os.path.join(BASE_DIR, 'rental/client_secrets.json')
            flow = InstalledAppFlow.from_client_secrets_file(
                SECRETS, scopes=SCOPES, redirect_uri="http://localhost:8080/")
            creds = flow.run_local_server()

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    calendars = {
        'T2': "burik7aclvhc7vsboh06c179uo@group.calendar.google.com",
        'T3': "fu7h30p0gk4a2p4nvo7nsbgpok@group.calendar.google.com"
    }

    return service, calendars


def get_bookings(place):
    service, calendars = build_service()
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    events_result = service.events().list(
        calendarId=calendars[place.name],
        timeMin=now,
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    events = events_result.get('items', [])
    if not events:
        logging.info('No upcoming events found.')
        reservation = None
    else:
        for event in events:
            reservation = {
                'place': place.name.strip(),
                'guest': event['summary'].strip(),
                'start': event['start'].get('dateTime', event['start'].get('date')).strip(),
                'end': event['end'].get('dateTime', event['end'].get('date')).strip()
            }

    return reservation


def synchronize(place):
    """
    Get a complete list of existing bookings in calendar
    Creates reservation if not in db, update if already in db
    Delete from db reservation deleted from cal
    """

    reservation = get_bookings(place)
    if not reservation:
        return
    place = get_object_or_404(m_place.Place, name=place.name)

    start = reservation['start']
    end = reservation['end']

    guest = Guest.objects.filter(name=reservation['guest'])
    if not guest.exists():
        guest = Guest.objects.create(name=reservation['guest'])
    else:
        guest = guest.first()

    db_booking = m_booking.Booking.objects.filter(
        guest=guest
    )
    if not db_booking.exists():
        m_booking.Booking.objects.create_booking(
            place=place,
            guest=guest,
            start=start,
            end=end
        )
    else:
        db_booking.place = place,
        db_booking.guest = guest,
        db_booking.start = start,
        db_booking.end = end


def get_bookings_from_db(place):
    """
    Synchronize with Master calendar via a call to synchronize_calendar
    Returns a list of all related place reservations
    """

    synchronize(place)
    booked_dates = m_booking.Booking.objects.filter(place=place)

    return [booking for booking in booked_dates]


def check_availability(place, start_date, end_date):
    """Checks if the related place is available during a given period."""

    bookings = get_bookings_from_db(place)
    for booking in bookings:
        if (booking.start <= start_date <= booking.end) or (booking.start <= end_date <= booking.end):
            return False

    return True


def update(reservation):
    """Push new reservation to master calendar."""
    # authenticate and build service

    service, calendars = build_service()
    start = reservation.start.strftime('%Y-%m-%d')
    end = reservation.end.strftime('%Y-%m-%d')

    service.events().insert(
        calendarId=calendars[reservation.place.name],
        body={
            "summary": reservation.guest.name,
            "description": reservation.message,
            "start": {
                "date": start
            },
            "end": {
                "date": end
            },
        }
    ).execute()
