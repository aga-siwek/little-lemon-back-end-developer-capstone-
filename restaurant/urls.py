from django.contrib import admin
from django.urls import path 
from .views import sayHello, index, MenuItemsView, SingleMenuItemView, Users, BookView, SingleBookView
from rest_framework.authtoken import views
  
urlpatterns = [ 
    path('', index, name='index'),
    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    path('users/', Users.as_view()),
    path('books', BookView.as_view()),
    path('books/<int:pk>', SingleBookView.as_view()),
    path('token-auth/', views.obtain_auth_token),
    
]
    