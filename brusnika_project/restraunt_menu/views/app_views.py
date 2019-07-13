from django.shortcuts import render, reverse
from django.views import View
from django.http import HttpResponse

from ..models import (MenuItem, Allergens, Category)


class MenuView(View):

    def context_value_handler(
            self: 'MenuView',
            categories: {'str': ['str']},
            category: 'str',
            meal: 'MenuItem'
        ) -> None:
        if category in categories:
            categories[category].append(meal.title)
        else:
            categories[category] = [meal.title]

    def get(self: 'MenuView', request: 'HttpRequest') -> 'HttpResponse':
        categories: {'str': ['str']} = {}
        menu = MenuItem.items.all()

        for meal in menu:
            meal: 'MenuItem' = meal
            category: 'Category' = meal.category

            if category:
                category: 'str' = category.name
                self.context_value_handler(categories, category, meal)

            else:
                category: 'str' = 'Без названия'
                self.context_value_handler(categories, category, meal)

        return render(request, 'restraunt_menu/list.html', context={'context': categories})


