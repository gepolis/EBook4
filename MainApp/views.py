from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import EventAddForm
from .models import Events, FeedBackQuestions
from django.contrib.auth.decorators import login_required
from Accounts.models import Account
import requests
import os

def index(request):
    return render(request, "main.html")

def feedback(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(name, email, phone, message)
        FeedBackQuestions.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )
        text = f"Имя: {name}\nEmail: {email}\nТелефон: {phone}\nСообщение: {message}\n\nВопрос от {email}\n\n#feedback"
        r = requests.get(f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_API_KEY}/sendMessage?chat_id={settings.BOT_CHAT_ID}&text={text}")
        print(r.url)
        print(r.text)
        return redirect("/")