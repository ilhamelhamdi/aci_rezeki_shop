from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from main.models import Category, Item
from main.forms import ItemForm, CategoryForm

def show_homepage(request):
    items = Item.objects.all()
    context = {
        'items': items,
    }
    return render(request, "index.html", context)

def show_about(request):
    context = {
        'author_name': "Ilham Abdillah Alhamdi",
        'class': "PBP B"
    }
    return render(request, "about.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    # When client hit submit -> Post
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect('/')

    context = {'form': form}
    return render(request, 'create_item.html', context)

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type="application/json")

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize('xml', data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(id=id)
    return HttpResponse(serializers.serialize('json', data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(id=id)
    return HttpResponse(serializers.serialize('xml', data), content_type="application/xml")

def show_html_by_id(request, id):
    data = Item.objects.get(id=id)
    context = {
        'data': data,
    }
    return render(request, "item_by_id.html", context)