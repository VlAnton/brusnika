from django.shortcuts import render, reverse
from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from ..models import (MenuItem, Allergens, Category)

import re


csrf_protected_method = method_decorator(csrf_protect)


class MenuView(View):

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

        return render(request, 'restraunt_menu/list.html', context={'context': categories})


class OrderView(TemplateView):
    template_name = 'restraunt_menu/bill.html'

    def get(self: 'OrderView', request: 'HttpRequest', *args, **kwargs) -> 'HttpResponse':
        path: str = request.get_full_path()
        context = {}

        meals = re.findall(r'\d+=\w+', path)

        for meal in meals:
            price, val = meal.split('=')
            context[val] = price

        return render(request, self.template_name, context={'context': context})