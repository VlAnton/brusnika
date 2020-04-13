from rest_framework import serializers

from restraunt_menu.models import MenuItem, Allergens, Category


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        exclude = ('allergens', 'category')

    def create(self, validated_data):  # TODO: обработка картинок
        allergens = Allergens.objects.filter(id=1)
        category = Category.objects.get(id=1)
        validated_data['category'] = category

        menu_item = MenuItem.objects.create(**validated_data)
        menu_item.allergens.set(allergens)
        return menu_item
