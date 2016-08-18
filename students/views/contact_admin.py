import logging

from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy

from django.contrib.auth.decorators import permission_required

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from studentsdb.settings import ADMIN_EMAIL

from django.conf import settings

class ContactForm(forms.Form):

	def __init__(self, *args, **kwargs):
		# call original initializatior
		super(ContactForm, self).__init__(*args, **kwargs)

		# this helper object allows us to customize form
		self.helper = FormHelper()

		# form tag attributes
		self.helper.form_class = 'form-horizontal'
		self.helper.form_method = 'post'
		self.helper.form_action = reverse('contact_admin')

		# twitter bootstrap styles
		self.helper.help_text_inline = True
		self.helper.html5_required = True
		self.helper.label_class = 'col-sm-2 control-label'
		self.helper.field_class = 'col-sm-10'

		# form buttons
		self.helper.add_input(Submit('send_button', ugettext_lazy(u"Send")))

	from_email = forms.EmailField(
		label=ugettext_lazy(u"Your e-mail"))

	subject = forms.CharField(
		label=ugettext_lazy(u"Title of the message"),
		max_length=128)

	message = forms.CharField(
		label=ugettext_lazy(u"Message"),
		max_length=2560,
		widget=forms.Textarea)


@permission_required('auth.add_user')
def contact_admin(request):
	# check if form was posted
	if request.method == 'POST':
		# create a form instanse and populate it with data from the request:
		form = ContactForm(request.POST)

		# check whether user data is valid:
		if form.is_valid():
			# send email
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			from_email = form.cleaned_data['from_email']

			try:
				send_mail(subject, message, from_email, [ADMIN_EMAIL])
			except Exception:
				message = _(u"There was an error on the server. Please, try again a bit later.")
				logger = logging.getLogger(__name__)
				logger.exception(message)
			else:
				message = _(u"Message was sended successfully")

			# redirect to same contact page with success message
			return HttpResponseRedirect(
                u'%s?status_message=%s' % (reverse('contact_admin'), message))

	# if there was not POS render blank form
	else:
		form = ContactForm()

	return render(request, 'contact_admin/form.html', {'form': form})
	
