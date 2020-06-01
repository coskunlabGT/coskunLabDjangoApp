from django.urls import path

from . import views


urlpatterns = [
    path('add-item/', views.add_Item, name = 'add-item'),
    path('get-item/', views.get_Item, name = 'get-item'),
    path('modify-item/', views.modify_Item, name = 'modify-item'),
    path('delete-item/', views.delete_Item, name = 'delete-item')

]
