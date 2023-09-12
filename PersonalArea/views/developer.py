from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from MainApp.models import FeedBackQuestions


def index(request):
    return render(request, "developer/index.html")
def feedbacks(request):
    fbs = FeedBackQuestions.objects.all().filter(answer__isnull=True)
    return render(request, "developer/feedbacks.html", {"fbs": fbs})

def view_feedback(request, fb_id):
    fb = FeedBackQuestions.objects.get(pk=fb_id)
    return render(request, "developer/view_feedback.html", {"fb": fb})
def send_feedback_answer(request, fb_id):
    if request.method == "POST":
        fb = FeedBackQuestions.objects.get(pk=fb_id)
        answer = request.POST.get("answer")
        send_mail("Ответ на Ваш вопрос", answer, settings.EMAIL_HOST_USER, [fb.email])
        fb.answer = answer
        fb.save()
        return redirect("/lk/feedbacks/")