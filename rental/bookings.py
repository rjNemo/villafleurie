import datetime
from rental.pricing import get_reservation_price
from django.shortcuts import get_object_or_404
from rental.models import Reservation, Place, Guest
import datetime
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os.path
import pickle
from villafleurie.settings import BASE_DIR


def synchronize_calendars(place):
    """
    Get a complete list of existing bookings in calendar
    Creates reservation if not in db, update if already in db
    Delete from db reservation deleted from cal
    """
    creds = None
    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            SECRETS = os.path.join(BASE_DIR, 'rental/client_secrets.json')
            flow = InstalledAppFlow.from_client_secrets_file(SECRETS, scopes=SCOPES,
                                                             redirect_uri="http://localhost:8080/")
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    calendar = place.name
    calendars = {
        'T2': "burik7aclvhc7vsboh06c179uo@group.calendar.google.com",
        'T3': "fu7h30p0gk4a2p4nvo7nsbgpok@group.calendar.google.com"
    }
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

    # for calendar in calendars:
    events_result = service.events().list(
        calendarId=calendars[calendar],
        timeMin=now,
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    events = events_result.get('items', [])
    if not events:
        print('No upcoming events found.')
    else:
        for event in events:
            reservation = {
                'place': calendar.strip(),
                'guest': event['summary'].strip(),
                'start': event['start'].get('dateTime', event['start'].get('date')).strip(),
                'end': event['end'].get('dateTime', event['end'].get('date')).strip()
            }

            place = get_object_or_404(Place, name=calendar)
            price = get_reservation_price(
                place, reservation['start'], reservation['end'])
            start = reservation['start']
            end = reservation['end']

            guest = Guest.objects.filter(name=reservation['guest'])
            if not guest.exists():
                guest = Guest.objects.create(name=reservation['guest'])
            else:
                # guest = guest[0]
                guest = guest.first()

            db_booking = Reservation.objects.filter(
                guest=guest
            )

            if not db_booking.exists():
                Reservation.objects.create(
                    place=place,
                    guest=guest,
                    start=start,
                    end=end,
                    price=price
                )
            else:
                db_booking.place = place,
                db_booking.guest = guest,
                db_booking.start = start,
                db_booking.end = end,
                db_booking.price = price


def get_bookings(place):
    """
    Synchronize with Master calendar via a call to synchronize_calendar
    Returns a list of all related place reservations
    """
    synchronize_calendars(place)
    booked_dates = Reservation.objects.filter(place=place)
    # if booking.place.name == f"{place.name}"]
    return [booking for booking in booked_dates]


def check_availability(place, start_date, end_date):
    """
    check if the related place is available during a given period
    """
    bookings = get_bookings(place)
    for booking in bookings:
        if (booking.start <= start_date <= booking.end) or (booking.start <= end_date <= booking.end):
            return False
    return True


if __name__ == '__main__':
    synchronize_calendars()