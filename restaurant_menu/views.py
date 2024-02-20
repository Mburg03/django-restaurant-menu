from django.shortcuts import render
from django.views import generic
from .models import Item, MEAL_TYPE


# Create your views here.
class MenuListView(generic.ListView):
    queryset = Item.objects.order_by('date_created')
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meals"] = MEAL_TYPE
        return context


class MenuItemDetailView(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"


class AboutView(generic.TemplateView):
    template_name = 'about_us.html'

