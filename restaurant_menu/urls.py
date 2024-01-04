from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuListView.as_view(), name='home')
]
