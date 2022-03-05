from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('filter/<str:category>', views.IndexView.as_view(), name='filter'),
    path('search/', views.IndexView.as_view(search=True), name='search'),
    path('contact/<int:pk>/', views.ContactView.as_view(), name='contact'),
    path('add/', views.add, name='add'),
    path('delete/', views.delete, name='delete'),
]