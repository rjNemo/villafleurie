import sys
from googleapiclient import sample_tools
import datetime
# from __future__ import print_function

# from google.auth.transport.requests import Request
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# import os.path
# import pickle

# from oauth2client import client

# from rental.models import Reservation


def get_bookings(place):
    """
    returns a list of all related place reservations
    """
    booked_dates = Reservation.objects.all()
    return [booking for booking in booked_dates if booking.place.name == f"{place.name}"]


def check_availability(place, start_date, end_date):
    """
    check if the related place is available during a given period
    """
    bookings = get_bookings(place)
    for booking in bookings:
        if (booking.start <= start_date <= booking.end) or (booking.start <= end_date <= booking.end):
            return False
    return True


def main1(argv):
    """
    Simple command-line sample for the Calendar API.
    Command-line application that retrieves the list of the user's calendars."""
    service, _ = sample_tools.init(
        argv, 'calendar', 'v3', __doc__, __file__,
        scope='https://www.googleapis.com/auth/calendar.readonly')

    calendars = {
        'T2': "burik7aclvhc7vsboh06c179uo@group.calendar.google.com",
        'T3': "fu7h30p0gk4a2p4nvo7nsbgpok@group.calendar.google.com"
    }

    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

    for calendar in calendars:
        print(f"Upcoming {calendar} events:")
        events_result = service.events().list(
            calendarId=calendars[calendar],
            timeMin=now,
            maxResults=10, singleEvents=True,
            orderBy='startTime').execute()
        events = events_result.get('items', [])
        reservation = {}
        if not events:
            print('No upcoming events found.')
        for index, event in enumerate(events):
            # start = event['start'].get('dateTime', event['start'].get('date'))
            # end = event['end'].get('dateTime', event['end'].get('date'))
            # print(start, end, event['summary'])
            reservation[index] = {
                'place': calendar,
                'guest': event['summary'],
                'start': event['start'].get('dateTime', event['start'].get('date')),
                'end': event['end'].get('dateTime', event['end'].get('date'))
            }
            print(reservation[index])


if __name__ == '__main__':
    main1(sys.argv)
