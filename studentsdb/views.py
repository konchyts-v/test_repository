from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import models
from django.forms import ModelForm

from django.views.generic import UpdateView, TemplateView

from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

from students.util import paginate

class EditForm(ModelForm):

	class Meta:
		model = models.User
		exclude = ['password', 'last_login', 'is_superuser', 'groups', 'user_permissions', 'is_staff', 'is_active']
		#fields = ['email', 'username']
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

def profile_page(request, pk):
	# 
	try:
		user = models.User.objects.get(pk=pk)
	except models.User.DoesNotExist:
		return HttpResponseRedirect(u'%s?status_message=%s' % (reverse('home'), _(u"User is not found")))
	return render(request, 'registration/profile.html', {'user': user})

def users_list(request):
	# get list of users
	users = models.User.objects.all()

	# try to order users list
	order_by = request.GET.get('order_by', '')
	if order_by in ('username',):
		users = users.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			users = users.reverse()

	# paginate users
	context = paginate(users, 10, request, {}, var_name='users')

	return render(request, 'registration/users_list.html', context)