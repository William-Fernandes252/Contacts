from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contact_id>/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('add/', views.add, name='add'),
    path('delete/', views.delete, name='delete'),
]