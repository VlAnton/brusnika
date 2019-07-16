from django.shortcuts import render, redirect, reverse
from django.views import View
from django.views.generic import TemplateView

from urllib.parse import unquote
from functools import reduce

from ..models import MenuItem, Allergens, Category

import re


class MenuView(TemplateView):
    template_name = 'restraunt_menu/list.html'

    def context_value_handler(
            self: 'MenuView',
            categories: {'str': ['str']},
            category: 'str',
            meal: 'MenuItem'
        ) -> None:
        if category in categories:
            categories[category].append({meal.title: meal.price})
        else:
            categories[category] = [{meal.title: meal.price}]

    def get(self: 'MenuView', request: 'HttpRequest') -> 'HttpResponse':
        categories: {'str': {'str': int}} = {}
        menu = MenuItem.items.all()

        for meal in menu:
            meal: 'MenuItem' = meal
            category: 'Category' = meal.category

            if category:
                self.context_value_handler(categories, category.name, meal)
            else:
                self.context_value_handler(categories, 'Без названия', meal)

        return render(request, self.template_name, context={'context': categories})


class OrderView(TemplateView):
    template_name = 'restraunt_menu/bill.html'

    def get(self: 'OrderView', request: 'HttpRequest', *args, **kwargs) -> 'HttpResponse':
        
        path: str = unquote(request.get_full_path())
        match: 're.Match' = re.search(r'\d+=.+', path)

        if match:
            meals: str = match.group(0).split('&')
            context = {
                'total': 0,
                'meals': []
            }

            for meal in meals:
                price, meal = meal.split('=')

                context['meals'].append(reduce(lambda x, y: f'{x} {y}', meal.split('_')))
                context['total'] += int(price)

            return render(request, self.template_name, context={'context': context})

        return redirect(reverse('menu-app'))