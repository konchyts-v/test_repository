from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from students.models.group import Group


class TestGroupList(TestCase):

    fixtures = ["groups_test_data.json"]

    def setUp(self):
        # remember test browser
        self.client = Client()

        # login as admin to access groups list
        self.client.login(username="admin", password="admin")

        # remembrer url to list page
        self.url = reverse("groups")

    def test_groups_list(self):
        # make request to the server to get our page
        response = self.client.get(self.url)

        # have we receive OK status from the server?
        self.assertEqual(response.status_code, 200)

        # do we have a group title on a page?
        self.assertIn("GroupA", response.content)

        # ensure we got a 3 groups, pagination limited is 3
        self.assertEqual(len(response.context['groups']), 3)

        # check if we have name of leader group1
        self.assertIn("Vitaliy Konchyts", response.content)

    def test_order_by(self):
        pass
        # make request to the server to get our page
        response = self.client.get(self.url, {'order_by': 'title'})

        # now check if we got proper order
        groups = response.context['groups']
        self.assertEqual(groups[0].title, "GroupA")
        self.assertEqual(groups[1].title, "GroupB")
        self.assertEqual(groups[2].title, "GroupC")

