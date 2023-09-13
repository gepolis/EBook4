import os

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from Accounts import decorators
from MainApp.models import FeedBackQuestions

@decorators.is_developer
def feedbacks(request):
    fbs = FeedBackQuestions.objects.all().filter(answer__isnull=True)
    return render(request, "developer/feedbacks.html", {"fbs": fbs, "archive": False, "section": "feedbacks"})

@decorators.is_developer
def feedbacks_archive(request):
    fbs = FeedBackQuestions.objects.all().filter(answer__isnull=False)
    return render(request, "developer/feedbacks.html", {"archive": True, "fbs": fbs, "section": "archive"})
@decorators.is_developer
def view_feedback(request, fb_id):
    fb = FeedBackQuestions.objects.get(pk=fb_id)
    return render(request, "developer/view_feedback.html", {"fb": fb, "section": "feedbacks"})
@decorators.is_developer
def send_feedback_answer(request, fb_id):
    if request.method == "POST":
        fb = FeedBackQuestions.objects.get(pk=fb_id)
        answer = request.POST.get("answer")
        send_mail("Ответ на Ваш вопрос", answer, settings.EMAIL_HOST_USER, [fb.email])
        fb.answer = answer
        fb.answer_by = request.user
        fb.save()
        return redirect("/lk/feedbacks/")

@decorators.is_developer
def get_logs(request):
    if True:
        lines = []
        logs = ""
        with open("/Ebook1/nohup.out", "r") as f:
            lines = f.readlines()
        logs = "<br>".join(lines)
        return render(request, "developer/logs.html", {"section": "logs", "logs": logs})
    return redirect("/lk/")