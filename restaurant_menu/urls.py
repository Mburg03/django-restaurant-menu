from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuListView.as_view(), name='home'),
    path('item/<int:pk>/', views.MenuItemDetailView.as_view(), name='menu_item'),
    path('about/', views.AboutView.as_view(), name='about'),
]
