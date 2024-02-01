from django.shortcuts import render
from django.views import generic
from .models import Item, MEAL_TYPE


# Create your views here.

# get teh data from database model and display it in html

# class based views


class MenuList(generic.ListView):
    queryset = Item.objects.order_by("date_created")
    template_name = 'index.html'

    # context is a dictionary made up of key and value
    def get_context_data(self, **kwargs):
        # context = {'meals': ['Pizza', 'Pasta'],
        #            'ingredient
        #
        #            s': ['things']}
        context = super().get_context_data(**kwargs)
        context['meals'] = MEAL_TYPE
        return context


class MenuItemDetails(generic.DetailView):
    model = Item
    template_name = 'menu_item_detail.html'


def about(request):
    return render(request, "about.html")


