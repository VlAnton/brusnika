from django.shortcuts import render
from django.views.generic import TemplateView

from restraunt_menu.models import MenuItem, Allergens, Category


class ListView(TemplateView):
    template_name = 'restraunt_menu/list.html'

    def get(self, request, *args, **kwargs):
        context = {'categories': Category.objects.all()}
        return render(request, self.template_name, context)


class OrderView(TemplateView):
    template_name = 'restraunt_menu/bill.html'

    def get_context_data(self, menu_item_ids, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        menu_items = MenuItem.objects.filter(id__in=menu_item_ids)
        menu_item_titles = menu_items.values_list('title', flat=True)
        menu_items_data = menu_items.values_list('title', 'price')
        context = {
            'titles': menu_item_titles,
            'order': [],
            'total': 0,
        }
        for title, price in menu_items_data:
            context['order'].append((price, Allergens.objects.filter(menu_items__title=title)))
            context['total'] += price

        return context

    def post(self, request, *args, **kwargs):
        order = request.POST.getlist('ordered')
        menu_item_ids = [int(item_id) for item_id in order]
        context = self.get_context_data(menu_item_ids)

        return render(request, self.template_name, context)
