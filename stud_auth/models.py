from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _ 


class StProfile(models.Model):
	""" To keep extra user data """
	# user maping
	user = models.OneToOneField(User)

	class Meta(object):
		verbose_name = _(u"User Profile")

	# extra user data
	mobile_phone = models.CharField(
		max_length=12,
		blank=True,
		verbose_name=_(u"Mobile Phone"),
		default='')

	address = models.CharField(
		max_length=25,
		blank=True,
		verbose_name=_(u"Address"),
		default='')

	passport_number = models.CharField(
		max_length=15,
		blank=True,
		verbose_name=_(u"Passport number"),
		default='')

	photo = models.ImageField(
		blank=True,
		verbose_name=_(u"Photo"),
		null=True)

	def __unicode__(self):
		return self.user.username