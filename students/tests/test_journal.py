from datetime import datetime, date

from django.test import TestCase, Client, override_settings
from django.core.urlresolvers import reverse

from students.models.student import Student
from students.models.group import Group
from students.models.monthjournal import MonthJournal

@override_settings(LANGUAGE_CODE='en')
class TestMonthJournalForm(TestCase):

    fixtures = ["journals_test_data.json"]

    def setUp(self):
        # remember test browser
        self.client = Client()

        # remember url
        self.url = reverse("journal")

    def test_journal_page_default_month(self):
        # login as admin to access journal page
        self.client.login(username="admin", password="admin")

        # get page
        response = self.client.get(self.url)

        # we have to get 200 status code
        self.assertEqual(response.status_code, 200)

        # check few fields
        self.assertIn("Journal", response.content)
        self.assertIn("Student", response.content)
        self.assertIn("Vitaliy", response.content)

    def test_journal_page_custom_month(self):
        # login as admin to access journal page
        self.client.login(username="admin", password="admin")

        # get page
        response = self.client.get(self.url, {"month": "2016-09-01"})

        # we have to get 200 status code
        self.assertEqual(response.status_code, 200)

        # check few fields
        self.assertIn("Journal", response.content)
        self.assertIn("Student", response.content)
        self.assertIn("Vitaliy", response.content)
        self.assertIn("September 2016", response.content)

    def test_post(self):
        # login as admin to access journal page
        self.client.login(username="admin", password="admin")

        # make post request
        response = self.client.post(self.url, {"pk":1, "date": "2016-09-01", "present": "1"})

        self.assertEqual(response.status_code, 200)
