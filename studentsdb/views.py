from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import models
from django.forms import ModelForm

from django.views.generic import UpdateView

from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

class EditForm(ModelForm):

	class Meta:
		model = models.User
		fields = ['email', 'username', 'first_name', 'last_name'] 

	def __init__(self, *args, **kwargs):
		# call original initializator
		super(EditForm, self).__init__(*args, **kwargs)

		#this helper object allows us to customize form
		self.helper = FormHelper(self)

		if kwargs['instance'] is None:
			edit_form = True
		else:
			edit_form = False

		# form tag attributes
		if edit_form:
			self.helper.form_acton = reverse('home')
		else:
			self.helper.form_action = reverse('edit_profile',
				kwargs={'pk': kwargs['instance'].id})

		self.helper.form_class = 'form-horizontal'
		self.helper.form_method = 'POST'

		# twitter bootstrap styles
		self.helper.help_text_inlibe = True
		self.helper.html5_required = True
		self.helper.label_class = 'col-sm-2 control-label'
		self.helper.field_class = 'col-sm-10'

		# form buttons
		submit = Submit('save_button', ugettext_lazy(u"Save"))
		self.helper.layout[-1] = FormActions(
			submit,
			Submit('cancel_button', _(u"Cancel"), css_class="btn btn-link"),
		)
		

class BaseProfileFormView(object):

    def get_success_url(self):
        return u'%s?status_message=%s' \
            % (reverse('profile'), _(u"Changes saved successfully"))

    def post(self, request, *args, **kwargs):
        # handle cancel button
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(reverse('profile') +
                u'?status_message=%s' % _(u"Changes were canceled"))
        else:
            return super(BaseProfileFormView, self).post(
                request, *args, **kwargs)

class ProfileUpdateView(BaseProfileFormView, UpdateView):
	model = models.User
	form_class = EditForm
	template_name = 'registration/edit_profile.html'