from django.test import TestCase, Client, override_settings
from django.core.urlresolvers import reverse

from students.models.group import Group
from students.models.student import Student

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


    def test_access(self):
        # try to access form as anonymous user
        response = self.client.get(self.url, follow=True)

        # we have to get 200 status code and login page
        self.assertEqual(response.status_code, 200)

        # check if we're on login form
        self.assertIn("Login", response.content)

        # check redirect url
        self.assertEqual(response.redirect_chain[0],
                         ('/users/login/?next=/groups/1/edit/', 302))


    def test_success(self):
        # login as admin to access group form edit
        self.client.login(username="admin", password="admin")

        # get form
        response = self.client.post(self.url, {"title": "Group3332", "leader": 2, "notes": "Hello world"}, follow=True)

        # check if status code equal 200
        self.assertEqual(response.status_code, 200)

        # test updated group details
        group = Group.objects.get(pk=1)
        student = Student.objects.get(pk=2)
        self.assertEqual(group.title, "Group3332")
        self.assertEqual(unicode(group), u"%s (%s %s)" % (group.title, group.leader.first_name, group.leader.last_name))
        self.assertEqual(group.notes, "Hello world")



