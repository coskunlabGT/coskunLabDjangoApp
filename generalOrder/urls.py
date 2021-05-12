from django.urls import path
from . import views
from . import message_views


urlpatterns = [

path('addOrder/', views.addGeneralOrder, name = 'addOrder'),
path('getOrders/', views.getGeneralOrders, name = 'getOrders'),

path('coskun/<str:order_id>/', message_views.getApproval, name = 'approval'),
path('approval/', message_views.AdminApprove, name = 'response'),

path('financeApproval/<str:order_id>/', message_views.FinanceApprove, name = 'finance-approval'),
path('financeDeliver/<str:order_id>/', message_views.FinanceDeliver, name = 'finance-deliver'),
path('financeCancel/<str:order_id>/', message_views.FinanceCancel, name = 'finance-cancel')

]