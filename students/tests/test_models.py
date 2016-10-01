from datetime import datetime, date
from django.test import TestCase

from students.models.student import Student
from students.models.group import Group
from students.models.monthjournal import MonthJournal


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

class JournalModelTests(TestCase):
	"""Test journal model"""

	def test_unicode(self):
		student = Student(first_name="Teest", last_name="Student")
		month_test = MonthJournal(student=student, date="2000-01-01")
		current_date = datetime.strptime(month_test.date, '%Y-%m-%d').date()
		month = date(current_date.year, current_date.month, 1)
		month_test = MonthJournal(student=student, date=month)

		self.assertEqual(unicode(month_test), 'Student: 1, 2000')