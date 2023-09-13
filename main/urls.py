# create urls routing for the main app
from django.urls import path
from main.views import show_homepage,show_shop

app_name = "main"

urlpatterns = [
    path('', show_homepage, name='show_homepage'),
    path('shop/', show_shop, name='show_shop'),
]