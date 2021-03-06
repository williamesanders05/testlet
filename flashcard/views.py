from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import *

# Create your views here.
def index(request):
    sets = Set.objects.all()
    return render(request, 'flashcard/index.html', {
        'sets':sets
    })

@login_required(login_url= "login")
def createset(request):
    if request.method == "POST":
        sets =  Set(
            title = request.POST["title"],
            owner = request.user.username,
            description = request.POST["description"]
        )
        sets.save()
        return HttpResponseRedirect(reverse("createterms", args=(sets.id)))
    return render(request, "flashcard/createset.html")

@login_required(login_url= "login")
def createterms(request, set_id):
    if request.method == "POST":
        term = Terms(
            term = request.POST["term"],
            definition = request.POST["definition"]
            image = request.POST["image"],
            set = set_id
        )
        term.save()
        return HttpResponseRedirect(reverse('index'))
    return render(request, "flashcard/createterm.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "flashcard/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "flashcard/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "flashcard/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "flashcard/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "flashcard/register.html")
