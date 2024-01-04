from django.shortcuts import render
from django.views import generic
from .models import Item


# Create your views here.
class MenuListView(generic.ListView):
    queryset = Item.objects.order_by('date_created')
    template_name = "index.html"


class MenuItemDetailView(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"
