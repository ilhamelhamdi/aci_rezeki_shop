# create urls routing for the main app
from django.urls import path
from main.views import show_homepage, create_item,create_item_ajax, get_items_json, get_items_xml, get_item_by_id_json,get_item_by_id_xml, show_about, show_item_detail, register, login_user, logout_user, update_item, delete_item

app_name = "main"

urlpatterns = [
    path('', show_homepage, name='show_homepage'),
    path('about/', show_about, name='show_about'),
    path('create-item/', create_item, name='create_item'),
    path('create-ajax/', create_item_ajax, name='create_item_ajax'),
    path('json/', get_items_json, name='get_items_json'),
    path('xml/', get_items_xml, name='get_items_xml'),
    path('json/<int:id>/', get_item_by_id_json, name='get_item_by_id_json'),
    path('xml/<int:id>/', get_item_by_id_xml, name='get_item_by_id_xml'),
    path('item/<int:id>/', show_item_detail, name='show_item_detail'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('update-item/<int:id>/', update_item, name='update_item'),
    path('delete-item/<int:id>/', delete_item, name='delete_item'),
]