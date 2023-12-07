from datetime import date
import datetime
import json
from django.shortcuts import redirect, render
from django.views.decorators.cache import cache_page
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from patyPlace.models import *
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.contrib.auth import logout
from .models import *
from geopy import Yandex
import ssl
import certifi
import geopy
from geopy.geocoders import Nominatim
from django.http import HttpResponse
ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx


def convertDt(dt):
    newdt = dt[6] + dt[7] + dt[8] + dt[9] + \
        "-" + dt[3] + dt[4] + "-" + dt[0] + dt[1]
    print(newdt)
    return newdt


# Create your views here.

class PatyUpdate(UpdateView):
    model = Party
    template_name = 'party/createParty.html'
    form_class = CreatePatyForm
    success_url = ''


class PatyDelete(DeleteView):
    model = Party
    template_name = 'party/deletePaty.html'
    success_url = '/'


def mypage(request):
    users = AuthUser.objects.filter(username=request.user)
    if len(users) != 0:
        userPaty = Party.objects.filter(creatorId=users[0])
        print(userPaty)
        return render(request, 'mypage/index.html', {'username': request.user, 'party': userPaty, 'title': 'Моя страница'})
    else:
        return render(request, 'mypage/index.html', {'username': request.user})


def index(request):
    partyses = {}
    oldPartys = {}
    user = request.user
    users = User.objects.filter(username=user)
    nearPartys = Party.objects.filter(dt__range=(
        date.today(), date.today() + datetime.timedelta(days=10)))[:3]
    oldPatys = Party2User.objects.select_related('partyField', 'userField').filter(
        partyField__dt__range=(date.today() - datetime.timedelta(days=10), date.today() - datetime.timedelta(days=1)))[:3]
    print(oldPatys.query)
    i = 0
    for nearParty in nearPartys:
        key = 'paty' + str(i)
        paty = {
            'title': nearParty.title,
            'description': nearParty.description,
            'dt': nearParty.dt,
            'countPeople': nearParty.countPeople,
            'images': nearParty.images,
        }
        partyses[key] = paty
        i += 1
    i = 0
    for oldParty in oldPatys:
        key = 'oldPaty' + str(i)
        oldPartyMap = {
            'title': oldParty.partyField.title,
            'description': oldParty.partyField.description,
            'dt': oldParty.partyField.dt,
            'countPeople': oldParty.partyField.countPeople,
            'images': oldParty.partyField.images,
        }
        oldPartys[key] = oldPartyMap
        i += 1
    if len(users) == 0:
        us = {}
        return render(request, 'party/index.html', {'title': "Главное окно", 'us': us, 'partyses': partyses, 'count': len(partyses), 'oldPartys': oldPartys, 'countOldPaty': len(oldPartys)})
    else:
        us = {
            'username': users[0].username,
            'name': users[0].first_name,
            'last_name': users[0].last_name,
            'email': users[0].email,
        }
        return render(request, 'party/index.html', {'title': "Главное окно", 'us': us, 'partyses': partyses, 'count': len(partyses), 'oldPartys': oldPartys, 'countOldPaty': len(oldPartys)})


def createParty(request):
    user = AuthUser.objects.get(username=request.user)
    if request.method == 'POST':
        form = CreatePatyForm(request.POST, request.FILES)
        params = form.data
        print(params)
        print(request.FILES)
        paty = Party(
            title=params['title'], description=params['description'], dt=convertDt(params['dt']), countPeople=params['countPeople'], adres=params['adres'], images=request.FILES['images'], creatorId=user)
        paty.save()
        HttpResponseRedirect('party/index.html')
    else:
        form = CreatePatyForm()
    return render(request, 'party/createParty.html', {'title': 'Создание', 'form': form})


class LoginUser(LoginView):
    form_class = LogInForm
    template_name = 'signIn/signIn.html'

    def get_default_redirect_url(self, **kwargs):
        url = super().get_success_url(**kwargs)
        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'signIn/signUp.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('signIn')


def jsonParty(request):
    places = Party.objects.filter(dt__range=(
        date.today(), date.today() + datetime.timedelta(days=365)))[:3]
    if request.method == 'GET':
        partys = []
        for i in places:
            party = []
            place = i.adres
            location = Yandex(
                api_key='7185e67d-b181-4cbd-ad9d-e548268ca289').geocode(place)
            party.append(i.title)
            party.append(i.description)
            party.append(str(i.dt))
            party.append(i.countPeople)
            party.append(location.longitude)
            party.append(location.latitude)
            party.append(str(i.images))
            partys.append(party)
            party = []

        response_data = {}
        response_data['message'] = 'allOk'
        response_data['partys'] = partys
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return HttpResponse(json.dumps([]), content_type="application/json")


def setcookie(request):
    html = HttpResponse("<h1>Какой нибудь заголовок</h1>")
    if request.COOKIES.get('visits'):
        html.set_cookie('dataflair', 'hello again')
        value = int(request.COOKIES.get('visits'))
        html.set_cookie('visits', value + 1)
    else:
        value = 1
        text = "hello one"
        html.set_cookie('visits', value)
        html.set_cookie('dataflair', text)
    return html


def showcookie(request):
    if request.COOKIES.get('visits') is not None:
        value = request.COOKIES.get('visits')
        text = request.COOKIES.get('dataflair')
        html = HttpResponse(
            "<center><h1>{0}<br>You have requested this page {1} times</h1></center>".format(text, value))
        html.set_cookie('visits', int(value) + 1)
        return html
    else:
        return redirect('/setcookie')


def delete_co(request):
    if request.COOKIES.get('visits'):
        response = HttpResponse("<h1>dataflair<br>Cookie deleted</h1>")
        response.delete_cookie("visits")
    else:
        response = HttpResponse(
            "<h1>dataflair</h1>need to create cookie before deleting")
    return response


def gofunc(request):
    if request.user.is_anonymous:
        print("somethink")
        return render(request, 'party/index.html')
    else:
        print(request.GET['paty'])
        paty = Party.objects.get(
            title=request.GET['paty'])
        print(paty)
        user = AuthUser.objects.get(username=request.user)
        doubleGet = Party2User.objects.filter(
            partyField=paty.pk).filter(userField=user.pk)
        if len(doubleGet) != 0:
            print('Юзер уже идет на пати')
            return render(request, 'party/isGoin.html')
        else:
            print(paty.pk)
            print(user.pk)
            party2user = Party2User(
                partyField=paty, userField=user)
            party2user.save()
            return render(request, 'party/index.html')
