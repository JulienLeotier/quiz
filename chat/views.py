from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.conf import settings

# Create your views here.
from django.shortcuts import render

from api.models import Categorie, Player, Score

class index(TemplateView):

  template_name = 'chat/index.html'

  def post(self, request, **kwargs):

    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        return HttpResponseRedirect( settings.LOGIN_REDIRECT_URL )

    return render(request, self.template_name)

def room(request, room_name):
    players = Player.objects.all()
    scores = Score.objects.all()
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'players': players,
        'scores': scores

    })


def admin(request, room_name):
    return render(request, 'chat/admin.html', {
        'room_name': room_name
    })

def display(request, room_name):
    players = Player.objects.all()
    scores = Score.objects.all()
    return render(request, 'chat/display.html', {
        'room_name': room_name,
        'players': players,
        'scores': scores
    })

def roomCategories(request, room_name):
    players = Player.objects.all()
    scores = Score.objects.all()
    categories = Categorie.objects.all()
    return render(request, 'chat/roomCategories.html', {
        'room_name': room_name,
        'players': players,
        'scores': scores,
        'categories': categories
    })



def onlyQuestion(request, room_name):
    players = Player.objects.all()
    scores = Score.objects.all()
    return render(request, 'chat/onlyQuestion.html', {
        'room_name': room_name,
        'players': players,
        'scores': scores,
        'categorie': room_name
    })

def adminCatagorie(request, room_name):
    players = Player.objects.all()
    scores = Score.objects.all()
    categories = Categorie.objects.all()
    return render(request, 'chat/adminCategories.html', {
        'room_name': room_name,
        'players': players,
        'scores': scores,
        'categories': categories
    })


def ref(request):
    return render(request, 'chat/ref.html')

def refadmin(request):
    return render(request, 'chat/refadmin.html')