from django.test import TestCase, Client, override_settings
from django.core.urlresolvers import reverse

from students.models.group import Group

@override_settings(LANGUAGE_CODE='en')
class TestGroupUpdateForm(TestCase):

    fixtures = ["groups_test_data.json"]

    def setUp(self):
        # remember test browser
        self.client = Client()

        # remember our url
        self.url = reverse("groups_edit", kwargs={'pk': 1})

    def test_form(self):
        # login as admin to access group form edit
        self.client.login(username="admin", password="admin")

        # get form and check few fields there
        response = self.client.get(self.url)

        # check page title, few fields titles and button on edit form
        self.assertIn("Group's Form", response.content)
        self.assertIn("Title", response.content)
        self.assertIn("Leader", response.content)
        self.assertIn('name="save_button"', response.content)
        self.assertIn('name="cancel_button"', response.content)