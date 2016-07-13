# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


def students_list(request):
    students = (
        {'id': 1,
         'first_name': u'Сергій',
         'last_name': u'Чередько',
         'ticket': 235,
         'image': 'img/sergiy.jpg'},
        {'id': 2,
         'first_name': u'Порохнавець',
         'last_name': u'Мортен',
         'ticket': 2123,
         'image': 'img/morten.jpg'},
         {'id': 3,
         'first_name': u'Кубов',
         'last_name': u'Роман',
         'ticket': 2123,
         'image': 'img/roma.jpg'},
    )
    return render(request, 'students/students_list.html',
        {'students': students})

def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
