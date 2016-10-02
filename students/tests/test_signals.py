import logging

from django.utils.six import StringIO
from django.test import TestCase

from students.models.student import Student
from students.models.group import Group


class StudentSignalsTests(TestCase):

	def test_log_student_updated_added_deleted_event(self):
		"""Check logging signal for newly created student"""
		# add own root handler to catch student signals output
		out = StringIO()
		handler = logging.StreamHandler(out)
		logging.root.addHandler(handler)

		# now create student, this should raise new message inside
		# our logger output file
		student = Student(first_name='Demo', last_name='Student', birthday="1990-01-01")
		student.save()

		# check output file content
		out.seek(0)
		self.assertEqual(out.readlines()[-1],
			'Student added: Demo Student (ID: %d)\n' % student.id)

		# now update existing student and check last line in out
		student.ticket = '12345'
		student.save()
		out.seek(0)
		self.assertEqual(out.readlines()[-1],
			'Student updated: Demo Student (ID: %d)\n' % student.id)


		# now delete existing student and check last line in out
		st_id = student.id
		student.delete()
		out.seek(0)
		self.assertEqual(out.readlines()[-1],
            'Student deleted: Demo Student (ID: %d)\n' % st_id)

		# remove our handler from root logger
		logging.root.removeHandler(handler)

class GroupSignalsTests(TestCase):

	def test_log_group_added_updated_deleted_event(self):
		"""Check logging signal for newly created group"""
		# add own root handler to catch group signals output
		out = StringIO()
		handler = logging.StreamHandler(out)
		logging.root.addHandler(handler)

		# now create group, this should raise new message inside
		# our logger output file
		group = Group(title="Test Group")
		group.save()

		# check output file content
		out.seek(0)
		self.assertEqual(out.readlines()[-1],
			'Group added: Test Group (ID: %d)\n' % group.id)

		# now update existing group and check last line in out
		group.notes = "Hello World"
		group.save()
		out.seek(0)
		self.assertEqual(out.readlines()[-1],
			'Group updated: Test Group (ID: %d)\n' % group.id)

		# now delete existing group and check last line in out
		gr_id = group.id
		group.delete()
		out.seek(0)
		self.assertEqual(out.readlines()[-1],
			'Group deleted: Test Group (ID: %d)\n' % gr_id)

		# remove our handler from root logger