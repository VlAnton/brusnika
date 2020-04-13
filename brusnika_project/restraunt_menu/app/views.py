import re
from urllib.parse import unquote
from functools import reduce

from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView

from restraunt_menu.models import MenuItem, Allergens, Category


class ListView(TemplateView):
    template_name = 'restraunt_menu/list.html'

    def get(self, request):
        categories = Category.objects.all()
        return render(request, self.template_name, {'categories': categories})


class OrderView(TemplateView):
    template_name = 'restraunt_menu/bill.html'

    def post(self, request, *args, **kwargs):
        order = request.POST.getlist('ordered')
        menu_item_ids = [int(item_id) for item_id in order]
        menu_items = MenuItem.objects.filter(id__in=menu_item_ids)

        context = {
            'order': menu_items.values_list('title', flat=True),
            'total': sum(menu_items.values_list('price', flat=True)),
        }
        return render(request, self.template_name, context)
