from rest_framework import serializers

from .models import (MenuItem, Category, Allergens)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')


class AllergensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergens
        fields = ('__all__')


class MenuItemSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False, max_length=100)
    calories = serializers.CharField(required=False)
    price = serializers.IntegerField(required=False)
    image = serializers.ImageField(required=False)
    list_of_allergens = serializers.CharField(required=False)
    category = serializers.CharField(required=False, max_length=200)

    class Meta:
        model = MenuItem
        fields = ('__all__')
    
    def validate(self: 'MenuItemSerializer', data: {}) -> {}:
        title = data.get('title')
        price = data.get('price')

        if not title:
            raise serializers.ValidationError('title is required')

        is_price_valid = (price and (
                isinstance(price, int) or 
                isinstance(price, float)
            )
        )

        if not is_price_valid:
            raise serializers.ValidationError('price is required')
            
        return data

    def create(self: 'MenuItemSerializer', validated_data: {}) -> 'MenuItem':
        title = validated_data.get('title')

        if MenuItem.items.filter(title=title):
                raise serializers.ValidationError('title is taken')

        allergens_str = validated_data.get('list_of_allergens')
        category_str = validated_data.get('category')

        allergens = None
        category = None

        if allergens_str:
            allergens = Allergens.allergens.filter(list_of_allergens=allergens_str).first()

            if not allergens:
                allergens = Allergens.allergens.create(list_of_allergens=allergens_str)
        
        if category_str:
            category = Category.categories.filter(name=category_str).first()

            if not category:
                category = Category.categories.create(name=category_str)

        validated_data['list_of_allergens'] = allergens
        validated_data['category'] = category

        return MenuItem.items.create(**validated_data)
