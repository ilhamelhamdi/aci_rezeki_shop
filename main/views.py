from django.core import serializers
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotAllowed
from django.urls import reverse
from main.models import Category, Item
from main.forms import ItemForm, CategoryForm

import datetime

@login_required(login_url='main:login')
def show_homepage(request):
    items = Item.objects.filter(user=request.user)
    count = Item.objects.filter(user=request.user).count()    # Jumlah item
    context = {
        'items': items,
        'item_count': count,
        'last_login': request.COOKIES.get('last_login'),
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
def update_item(request, id):
    
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')

    context = {'form': form}
    return render(request, 'update_item.html', context)

@login_required(login_url='main:login')
def delete_item(request, id):
    if request.method != "DELETE":
        return HttpResponseNotAllowed(['DELETE'])
    item = Item.objects.get(id=id)
    if item.user != request.user:
        messages.error(request, 'You are not authorized to delete this item!')
        return redirect('main:show_homepage')
    item.delete()
    messages.success(request, 'Item has been deleted!')
    return redirect('main:show_homepage')

@login_required(login_url='main:login')
def show_json(request):
    data = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', data), content_type="application/json")

@login_required(login_url='main:login')
def show_xml(request):
    data = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('xml', data), content_type="application/xml")

@login_required(login_url='main:login')
def show_json_by_id(request, id):
    data = Item.objects.filter(user=request.user, id=id)
    return HttpResponse(serializers.serialize('json', data), content_type="application/json")

@login_required(login_url='main:login')
def show_xml_by_id(request, id):
    data = Item.objects.filter(user=request.user, id=id)
    return HttpResponse(serializers.serialize('xml', data), content_type="application/xml")

@login_required(login_url='main:login')
def show_html_by_id(request, id):
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
