from django.test import TestCase

from students.models.student import Student
from students.models.group import Group


class StudentModelTests(TestCase):
	"""Test student model"""

	def test_unicode(self):
		student = Student(first_name="Test", last_name="Student")
		self.assertEqual(unicode(student), u'Test Student')

class GroupModelTests(TestCase):
	"""Test group model"""

	def test_unicode(self):
		group1 = Group(title="Test Group")
		student = Student(first_name="Demo", last_name="Student")
		group2 = Group(title="Demo Group", leader=student)

		self.assertEqual(unicode(group1), 'Test Group')
		self.assertEqual(unicode(group2), 'Demo Group (Demo Student)')