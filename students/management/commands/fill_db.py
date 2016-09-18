from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from students.models.student import Student
from students.models.group import Group

class Command(BaseCommand):
	args = '<model_name=number model_name=number ...>'
	help = "Random create students/groups/user in database"



	def handle(self, *args, **kwargs):
		