from rest_framework import serializers

from restraunt_menu.models import (MenuItem, Category, Allergens)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')


class AllergensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergens
        fields = ('__all__')


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('__all__')
    
    def validate(self, data):
        title = data.get('title')
        price = data.get('price')

        if not title:
            raise serializers.ValidationError('title is required')

        is_price_valid = price and isinstance(price, (float, int))
        if not is_price_valid:
            raise serializers.ValidationError('price is required')
        return data

    def create(self, validated_data):
        title = validated_data.get('title')
        if MenuItem.items.filter(title=title):
            raise serializers.ValidationError('title is taken')

        allergens_str = validated_data.get('list_of_allergens', '')
        category_str = validated_data.get('category', '')

        allergens = Allergens.allergens.filter(list_of_allergens=allergens_str).first()
        if not allergens:
            allergens = Allergens.allergens.create(list_of_allergens=allergens_str)
        
        category = Category.categories.filter(name=category_str).first()
        if not category:
            category = Category.categories.create(name=category_str)

        validated_data['list_of_allergens'] = allergens
        validated_data['category'] = category

        return MenuItem.items.create(**validated_data)
