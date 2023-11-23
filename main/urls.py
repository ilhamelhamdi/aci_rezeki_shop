# create urls routing for the main app
from django.urls import path
import main.views as views

app_name = "main"

urlpatterns = [
    path('', views.show_homepage, name='show_homepage'),
    path('about/', views.show_about, name='show_about'),
    path('create-item/', views.create_item, name='create_item'),
    path('json/', views.get_items_json, name='get_items_json'),
    path('xml/', views.get_items_xml, name='get_items_xml'),
    path('json/<int:id>/', views.get_item_by_id_json, name='get_item_by_id_json'),
    path('xml/<int:id>/', views.get_item_by_id_xml, name='get_item_by_id_xml'),
    path('item/<int:id>/', views.show_item_detail, name='show_item_detail'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('update-item/<int:id>/', views.update_item, name='update_item'),
    path('delete-item/<int:id>/', views.delete_item, name='delete_item'),
    path('api/login/', views.login, name='login_api'),
    path('api/logout/', views.logout, name='logout_api'),
    path('api/register/', views.register, name='register_api'),
]