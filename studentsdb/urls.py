"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from .settings import MEDIA_ROOT, DEBUG
from students.views.students import StudentDeleteView
from students.views.groups import GroupAddView, GroupUpdateView, GroupDeleteView, groups_list
from students.views.journal import JournalView
from views import ProfileUpdateView

from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from django.views.generic.base import RedirectView, TemplateView


urlpatterns = [
	# Students urls
	url(r'^$', 'students.views.students.students_list', name='home'),
    url(r'^students/add/$', 'students.views.students.students_add', name='students_add'),
    url(r'^students/(?P<pk>\d+)/edit/$', 'students.views.students.students_edit', name='students_edit'),
    url(r'^students/(?P<pk>\d+)/delete/$', StudentDeleteView.as_view(), name='students_delete'),
    
    # Groups urls
    url(r'^groups/$', login_required(groups_list), name='groups'),
    url(r'^groups/add/$', login_required(GroupAddView.as_view()), name='groups_add'),
    url(r'^groups/(?P<pk>\d+)/edit/$', login_required(GroupUpdateView.as_view()), name='groups_edit'),
    url(r'^groups/(?P<pk>\d+)/delete/$', login_required(GroupDeleteView.as_view()), name='groups_delete'),
    
    url(r'^admin/', include(admin.site.urls)),

    # Contact Admin Form
    url(r'^contact-admin/$', 'students.views.contact_admin.contact_admin', name='contact_admin'),
    # Journal Page
    url(r'^journal/(?P<pk>\d+)?/?$', login_required(JournalView.as_view()), name='journal'),

    # User Related urls
    url(r'^users/profile/$', login_required(TemplateView.as_view(template_name='registration/profile.html')), name='profile'),
    url(r'^users/(?P<pk>\d+)/edit_profile/$', login_required(ProfileUpdateView.as_view()), name='edit_profile'),
    url(r'^users/logout/$', auth_views.logout, kwargs={'next_page': 'home'},
        name='auth_logout'),
    url(r'^register/complete/$', RedirectView.as_view(pattern_name='home'),
        name='registration_complete'),
    url(r'^users/', include('registration.backends.simple.urls',
        namespace='users')),

    # Social Auth Related urls
    url('^social/', include('social.apps.django_app.urls', namespace='social')),
]

if DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': MEDIA_ROOT})
    ]

js_info_dict = {
    'packages': ('my.package',),
}

urlpatterns += [
    url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog', js_info_dict),
]


