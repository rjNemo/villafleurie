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


def synchronize_calendars():
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
            singleEvents=True,
            orderBy='startTime').execute()
        events = events_result.get('items', [])
        if not events:
            print('No upcoming events found.')
        else:
            # reservation = {}
            for event in events:
                reservation = {
                    'place': calendar,
                    'guest': event['summary'],
                    'start': event['start'].get('dateTime', event['start'].get('date')),
                    'end': event['end'].get('dateTime', event['end'].get('date'))
                }
                print(reservation)

# if booking not in db -> create
# if booking in db and modification_date_cal > update_date_db -> update
# try : create/update
# except : send a log message
                try:
                    place = get_object_or_404(Place, name=calendar)
                    price = get_reservation_price(
                        place, reservation['start'], reservation['end'])
                    # trouver si guest existe déjà, créer sinon
                    guest = Guest.objects.create(name=reservation['guest'])
                    start = reservation['start']
                    end = reservation['end']
                    Reservation.objects.create(
                        place=place,
                        guest=guest,
                        start=start,
                        end=end,
                        price=price
                    )
                except:
                    print(
                        f"######## ERROR ! Can't create {guest} reservation ########")


if __name__ == '__main__':
    synchronize_calendars()
