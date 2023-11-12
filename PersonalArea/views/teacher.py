import random
import threading
import uuid
from datetime import datetime

import six
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template

from Accounts.models import Account
from MainApp.models import *
from django.utils.formats import localize

from PersonalArea.forms import *
from Accounts.forms import NewBuildingForm
from Accounts.models import Building
from Accounts import decorators
import io
import xlsxwriter
import pandas as pd

@decorators.is_teacher
def create_classroom(request):
    if ClassRoom.objects.all().filter(teacher=request.user).exists():
        return redirect("/lk/")
    if request.method == "GET":
        form = NewClassRoom()
    else:
        form = NewClassRoom(request.POST)
        if form.is_valid():
            if form.unique():
                classroom = form.save(commit=False)
                classroom.teacher = request.user
                classroom.save()
            else:
                messages.error(request,
                               "Данный класс уже существует. Если вы являетесь классным руководителем класса который уже существует, обратитесь к администрации.")
                return render(request, "teacher/create_classroom.html", {"form": form, "section": "classroom"})
        return redirect("/lk/")
    return render(request, "teacher/create_classroom.html", {"form": form, "section": "classroom"})


@decorators.is_teacher
def create_invite(request):
    if ClassRoom.objects.all().filter(teacher=request.user).exists():
        classroom = ClassRoom.objects.get(teacher=request.user)
        return render(request, "teacher/invite.html", {"uuid": classroom.uuid, "section": "classroom"})
    else:
        return redirect("/lk/classroom/create/")


@decorators.is_teacher
def update_invite(request):
    if ClassRoom.objects.all().filter(teacher=request.user).exists():
        classroom = ClassRoom.objects.get(teacher=request.user)
        classroom.uuid = uuid.uuid4()
        classroom.save()
        return redirect("/lk/classroom/invite/create/")
    else:
        return redirect("/lk/classroom/create/")


@decorators.is_teacher
def invite_classroom_event(request, id):
    if ClassRoom.objects.all().filter(teacher=request.user).exists():
        classroom = ClassRoom.objects.get(teacher=request.user)
        event = Events.objects.get(pk=id)
        for member in classroom.member.all():
            if not EventsMembers.objects.all().filter(user=member, event=event).exists():
                vol = EventsMembers.objects.create(user=member, is_active=True)
                event.volunteer.add(vol)
        messages.success(request, "Вы успешно пригласили класс на мероприятие.")
        return redirect("/lk/events/")
    else:
        return redirect("/lk/classroom/create/")


@decorators.is_teacher
def classroom_students(request):
    if ClassRoom.objects.all().filter(teacher=request.user).exists():
        classroom = ClassRoom.objects.get(teacher=request.user)
        members = classroom.member.all()
        return render(request, "teacher/students.html", {"members": members, "section": "classroom"})
    else:
        return redirect("/lk/classroom/create/")


@decorators.is_teacher
def classroom_view_student(request, user):
    if ClassRoom.objects.all().filter(teacher=request.user).exists():
        classroom = ClassRoom.objects.get(teacher=request.user)
        if classroom.member.all().filter(pk=user).exists():
            user = classroom.member.get(pk=user)
            events = Events.objects.all().filter(volunteer__user=user)
            return render(request, "teacher/view_student.html",
                          {"student": user, "events": events, "section": "classroom"})
        else:
            return redirect("/lk/classroom/students/")
    else:
        return redirect("/lk/classroom/create/")


def classroom_students_upload(request):
    if request.method == "POST":
        t = threading.Thread(target=students_upload_thr, args=(request,))
        t.start()
        messages.success(request, "Начинаю загрузку, пожалуйста, подождите!")
        return redirect("/lk/classroom/students/")
    else:
        return render(request, "teacher/students_upload.html", {"section": "classroom"})

def students_upload_thr(request):
    file = request.FILES["file"]
    file_lines = file.read().decode("utf-8").splitlines()
    class_room = ClassRoom.objects.get(teacher=request.user)
    for row in file_lines:
        d = row.split(" ")
        sn, fn, mn = d[0], d[1], d[2]

        if not Account.objects.filter(first_name=fn, middle_name=mn, second_name=sn,
                                      account__classroom=class_room).exists():
            usr = Account.objects.create(first_name=fn, middle_name=mn, second_name=sn, role="student")
            usr.building = request.user.building

            random_word = ['венок', 'забава', 'прыгун', 'флажок', 'свет', 'арена', 'цвет', 'стиль', 'роза']
            word = random.choice(random_word)
            random_number = random.randint(1000, 9999)
            first_number = random.randint(0, 1)
            if first_number == 0:
                password = word + str(random_number)
            else:
                password = str(random_number) + word
            usr.set_password(password)
            usr.username = f"student_{usr.id}"
            usr.save()
            class_room.member.add(usr)
            clu = ClassRoomTeacherAuthUser.objects.create(user=usr, classroom=class_room, password=password)
            clu.save()
    messages.success(request, "Загрузка завершена!")
def students_list2pdf(request):
    if ClassRoom.objects.all().filter(teacher=request.user).exists():
        classroom = ClassRoom.objects.get(teacher=request.user)
        members = ClassRoomTeacherAuthUser.objects.all().filter(classroom=classroom)
        return render(request, "teacher/students_pdf.html", {"members": members, "section": "classroom", "classroom": classroom})
    else:
        return redirect("/lk/classroom/create/")