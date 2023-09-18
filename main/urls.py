# create urls routing for the main app
from django.urls import path
from main.views import show_homepage, create_item, show_json, show_xml, show_json_by_id, show_xml_by_id

app_name = "main"

urlpatterns = [
    path('', show_homepage, name='show_homepage'),
    path('create_item/', create_item, name='create_item'),
    path('json/', show_json, name='show_json'),
    path('xml/', show_xml, name='show_xml'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
]