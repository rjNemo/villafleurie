from django.test import TestCase

import rental.services.calendar as calendar


class CalendarTestCase(TestCase):

    def test_CalendarBuild(self):
        obj = calendar.build_service()
