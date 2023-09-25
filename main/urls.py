# create urls routing for the main app
from django.urls import path
from main.views import show_homepage, create_item, show_json, show_xml, show_json_by_id, show_xml_by_id, show_about, show_html_by_id, register, login_user, logout_user

app_name = "main"

urlpatterns = [
    path('', show_homepage, name='show_homepage'),
    path('about/', show_about, name='show_about'),
    path('create-item/', create_item, name='create_item'),
    path('json/', show_json, name='show_json'),
    path('xml/', show_xml, name='show_xml'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('item/<int:id>/', show_html_by_id, name='show_html_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout')
]