from django.urls import path

from . import views

urlpatterns = [
    path('get-Users/', views.getUsers, name='get-Users'),
    path('add-User/', views.addUser, name='add-User'),
    path('delete-User/', views.deleteUser, name='delete-User'),
    path('update-User/', views.updateUser, name='update-User'),
    path('add-Research/', views.addResearch, name='add-Research'),
    path('get-Research/', views.getResearch, name='get-Research'),
    path('get-Dashboard/', views.getDashboard, name='get-Dashboard'),
    path('add-ResearchtoDashboard/', views.addResearchtoDashboard, name='add-ResearchtoDashboard'),
<<<<<<< HEAD
    path('get-allDashboards/', views.getAllDashboards, name='get-allDashboards'),
=======
    path('get-allDashboards/', views.getAllDashboards, name='get-allDasboards'),
>>>>>>> upstream/master
    path('delete-ResearchfromDashboard/', views.deleteResearchfromDashboard, name='delete-ResearchfromDashboard')
]
