from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import ModelForm
from django.views.generic import UpdateView, DeleteView
from django.utils.translation import ugettext as _
from django.utils.translation import activate
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.utils import translation
from django.conf import settings

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

from ..models.student import Student
from ..models.group import Group
from ..util import paginate, get_current_group



def students_list(request):
    # check if we need to show only one group of students

    current_group = get_current_group(request)
    if current_group:
        students = Student.objects.filter(student_group=current_group).order_by('last_name')
    else:
        # otherwise show all students
        students = Student.objects.all().order_by('last_name')

    # try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

    # paginate students
    context = paginate(students, 3, request, {}, var_name='students')

    #user_language = 'uk'
    #translation.activate(user_language)
    
    response = render(request, 'students/students_list.html', context)
    #response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    return response
    
@login_required
def students_add(request):
    # was form posted?
    if request.method == "POST":
        # was form add button clicked?
        if request.POST.get('add_button') is not None:

            # TODO: validate input from user
            errors = {}
            # validate student data will go here
            data = {'middle_name': request.POST.get('middle_name'),
                    'notes': request.POST.get('notes')}

            # validate user input
            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = _(u"First Name field is required")
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = _(u"Last Name field is required")
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday', '').strip()
            if not birthday:
                errors['birthday'] = _(u"Birthday field is required")
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors['birthday'] = _(u"Enter the corrent type of date")
                else:
                    data['birthday'] = birthday
            
            ticket = request.POST.get('ticket', '').strip()
            if not ticket:
                errors['ticket'] = _(u"Ticket number is reuired")
            else:
                data['ticket'] = ticket

            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = _(u"Check the group and student")
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    errors['student_group'] = _(u"Check the correct group")
                else:
                    data['student_group'] = groups[0]

            photo = request.FILES.get('photo')
            if photo:
                destination = photo.name[-3:]
                destinations = ('jpg', 'bmp', 'png', 'gif')
                if destination in destinations:
                    if photo.size <= 2000000:
                        data['photo'] = photo
                    else:
                        errors['photo'] = _(u"Photo size larger than 2 MB")
                else:
                    errors['photo'] = _(u"Check correct format of photo")

            # save student        
            if not errors:
                student = Student(**data)
                student.save()

                # redirect user to students list
                return HttpResponseRedirect(
                    u'%s?status_message=%s' % (reverse('home'), _(u"Student added successfully!")))

            else:
                # render form with errors and previous user input
                return render(request, 'students/students_add.html',
                    {'groups': Group.objects.all().order_by('title'),
                    'errors': errors})
        elif request.POST.get('cancel_button') is not None:
            # redirect to home page on cancel button
            return HttpResponseRedirect(
                u'%s?status_message=%s' % (reverse('home'), _(u"Student added was canceled!")))
    else:
        # initial form render
        return render(request, 'students/students_add.html',
            {'groups': Group.objects.all().order_by('title')})

@login_required
def students_edit(request, pk):
    # was form posted?
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponseRedirect(u'%s?status_message=%s' % (reverse('home'), _(u"Student is not found")))
    if request.method == "POST":
        # was form add button clicked?
        if request.POST.get('save_button') is not None:
            

            # TODO: validate input from user
            errors = {}
            # validate student data will go here
            middle_name = request.POST.get('middle_name')
            notes = request.POST.get('notes')

            # validate user input
            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = _(u"First Name field is required")

            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = _(u"Last Name field is required")

            birthday = request.POST.get('birthday', '').strip()
            if not birthday:
                errors['birthday'] = _(u"Birthday field is required")
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors['birthday'] = _(u"Enter the corrent type of date")
            
            ticket = request.POST.get('ticket', '').strip()
            if not ticket:
                errors['ticket'] = _(u"Ticket number is reuired")

            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = _(u"Check the group and student")
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    errors['student_group'] = _(u"Check the correct group")

            photo = request.FILES.get('photo')
            if photo:
                destination = photo.name[-3:]
                destinations = ('jpg', 'bmp', 'png', 'gif')
                if destination in destinations:
                    if photo.size <= 2000000:
                        passzzzz
                    else:
                        errors['photo'] = _(u"Photo size larger than 2 MB")
                else:
                    errors['photo'] = _(u"Check correct format of photo")

            # save student        
            if not errors:
                #student = Student(**data)
                student.first_name = first_name
                student.last_name = last_name
                student.middle_name = middle_name
                student.birthday = birthday
                student.ticket = ticket
                student.student_group = groups[0]
                student.photo = photo
                group_of_students = Group.objects.filter(leader=student)
                if len(group_of_students) > 0 and student.student_group != group_of_students[0]:
                    errors['student_group'] = _(u"Student is leader of other group")
                    return render(request, 'students/students_edit.html',
                        {'groups': Group.objects.all().order_by('title'),
                        'errors': errors, 'student': student})
                else:
                    student.save()  

                # redirect user to students list
                return HttpResponseRedirect(
                     u'%s?status_message=%s' % (reverse('home'), _(u"Student updated successfully!")))

            else:
                # render form with errors and previous user input
                return render(request, 'students/students_edit.html',
                    {'groups': Group.objects.all().order_by('title'),
                    'errors': errors, 'student': student})

        elif request.POST.get('cancel_button') is not None:
            # redirect to home page on cancel button
            return HttpResponseRedirect(
                u'%s?status_message=%s' % (reverse('home'), _(u"Student added was canceled!")))
    else:
        # initial form render
        return render(request, 'students/students_edit.html',
            {'groups': Group.objects.all().order_by('title'), 'student': student})

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/students_confirm_delete.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(StudentDeleteView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return  u'%s?status_message=%s' % (reverse('home'), _(u"Student updated successfully!"))
