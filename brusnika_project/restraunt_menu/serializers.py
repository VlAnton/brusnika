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

    def validate_title(self: 'MenuItemSerializer', value: str) -> str:
        if not value:
            if not self.instance:
                raise serializers.ValidationError(
                    'title is missing or incorrect'
                )

            return self.instance.price
        return value

    def validate_price(self: 'MenuItemSerializer', value: int) -> int:
        is_price_valid = (value and (
                isinstance(value, int) or 
                isinstance(value, float)
            )
        )

        if not is_price_valid:
            if not self.instance:
                raise serializers.ValidationError(
                    'price is missing or incorrect'
                )

            return self.instance.price
        return value

    def update(self: 'MenuItemSerializer', instance: 'MenuItem', validated_data: {}) -> 'MenuItem':
        instance.title = validated_data.get('title', instance.title)
        instance.calories = validated_data.get('calories', instance.calories)
        instance.price = validated_data.get('price', instance.price)
        instance.image = validated_data.get('image', instance.image)
        instance.list_of_allergens = validated_data.get(
            'list_of_allergens',
            instance.list_of_allergens
        )
        instance.category = validated_data.get('category', instance.category)

        instance.save()

        return instance

    def create(self: 'MenuItemSerializer', validated_data: {}) -> 'MenuItem':
        alergens_str = validated_data.get('list_of_allergens')
        category_str = validated_data.get('category')

        alergens = None
        category = None

        if alergens_str:
            alergens = Allergens.alergens.filter(list_of_allergens=alergens_str).first()

            if not alergens:
                alergens = Allergens.alergens.create(list_of_allergens=alergens_str)
        
        if category_str:
            category = Category.categories.filter(name=category_str).first()

            if not category:
                category = Category.categories.create(name=category_str)

        validated_data['list_of_allergens'] = alergens
        validated_data['category'] = category

        return MenuItem.items.create(**validated_data)
