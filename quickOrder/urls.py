from django.urls import path

from . import views


urlpatterns = [
    path('inventory/', views.getInventory, name = 'inventory'),
    path('add-item/', views.addItem, name = 'add-item'),
    path('get-item/<str:pk>/', views.getItem, name = 'get-item'),
    path('update-item/<str:pk>/', views.updateItem, name = 'update-item'),
    path('delete-item/<str:pk>/', views.deleteItem, name = 'delete-item')

]
