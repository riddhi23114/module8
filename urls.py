from django.urls import path 
from rest_framework.authtoken.views import obtain_auth_token
from . import views


# url / app level 

urlpatterns = [
    path('',views.index,name='index'),
    path('',views.index,name='home'),
    path('menu/', views.MenuItemsView.as_view(),name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    
    
]