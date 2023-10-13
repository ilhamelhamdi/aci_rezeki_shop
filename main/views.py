from django.core import serializers
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponse, HttpResponseServerError, HttpResponseForbidden
from django.urls import reverse
from main.models import Category, Item
from main.forms import ItemForm, CategoryForm

import datetime


@login_required(login_url='main:login')
def show_homepage(request):
    form = ItemForm()
    context = {
        'last_login': request.COOKIES.get('last_login'),
        'form': form,
    }
    return render(request, "index.html", context)

def show_about(request):
    context = {
        'author_name': "Ilham Abdillah Alhamdi",
        'class': "PBP B"
    }
    return render(request, "about.html", context)

@login_required(login_url='main:login')
def create_item(request):
    form = ItemForm(request.POST or None)

    # When client hit submit -> Post
    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect('/')

    context = {'form': form}
    return render(request, 'create_item.html', context)

@login_required(login_url='main:login')
def create_item_ajax(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    try:
        form = ItemForm(request.POST or None)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return HttpResponse('Item has been created', status=201)
        return HttpResponseBadRequest('Invalid data')
    except:
        return HttpResponseServerError()

@login_required(login_url='main:login')
def update_item(request, id):
    if request.method != "POST":
        return HttpResponseNotAllowed(['POST'])
    
    item = Item.objects.get(id=id, user=request.user)

    data = request.POST.dict()
    # item.name = data['name'] if 'name' in data else item.name
    # item.amount = int(data['amount']) if 'amount' in data else item.amount
    # item.name = data['name'] if 'name' in data else item.name

    # setattr(item, 'amount', '9')
    # item.amount = '11'
    # amount = getattr(item, 'amount')
    print(item.amount)
    # item.save()
    # for x in request.POST:
        # item[x] = request.POST[x]
    # item.save()

    return HttpResponse('OK')
    # if form.is_valid():
    #     form.save()
    #     return HttpResponseRedirect(f'/item/{id}')  # reload

@login_required(login_url='main:login')
def delete_item(request, id):
    if request.method != "DELETE":
        return HttpResponseNotAllowed(['DELETE'])
    item = Item.objects.get(id=id)
    if item.user != request.user:
        return HttpResponseForbidden('Unauthorized')
    item.delete()
    return HttpResponse('Deleted')

@login_required(login_url='main:login')
def get_items_json(request):
    data = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', data), content_type="application/json")

@login_required(login_url='main:login')
def get_items_xml(request):
    data = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('xml', data), content_type="application/xml")

@login_required(login_url='main:login')
def get_item_by_id_json(request, id):
    data = Item.objects.filter(user=request.user, id=id)
    return HttpResponse(serializers.serialize('json', data), content_type="application/json")

@login_required(login_url='main:login')
def get_item_by_id_xml(request, id):
    data = Item.objects.filter(user=request.user, id=id)
    return HttpResponse(serializers.serialize('xml', data), content_type="application/xml")

@login_required(login_url='main:login')
def show_item_detail(request, id):
    data = Item.objects.filter(user=request.user, id=id)
    context = {
        'data': data,
    }
    return render(request, "item_by_id.html", context)

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() # Save user to database
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            response = HttpResponseRedirect(reverse("main:show_homepage"))
            response.set_cookie('last_login',str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out!')
    response = HttpResponseRedirect(reverse("main:login"))
    response.delete_cookie('last_login')
    return response
