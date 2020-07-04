from django.urls import path
from . import views

urlpatterns = [
    path('get_list/', views.get_list, name='get_list'),
    path('get_reading/<int:sr_num>/', views.get_reading, name='get_reading'),
    path('get_latest/', views.get_latest, name='get_latest'),
    path('post_reading/', views.post_reading, name='post_reading'),
    path('delete_readings/', views.delete_readings, name='delete_readings')
]
