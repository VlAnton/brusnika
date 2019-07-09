from rest_framework import serializers

from .models import (MenuItem, Category, Allergens)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AllergensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergens
        fields = '__all__'


class MenuItemSerializer(serializers.Serializer):
    title = serializers.CharField(required=False, max_length=100)
    calories = serializers.CharField(required=False)
    price = serializers.IntegerField(required=False)
    image = serializers.ImageField(required=False)
    list_of_allergens = AllergensSerializer(required=False)
    category = CategorySerializer(required=False)

    def validate_title(self: 'MenuItemSerializer', value: str):
        if not value:
            if not self.instance:
                raise serializers.ValidationError(
                    'title is missing or incorrect'
                )

            return self.instance.price
        return value

    def validate_price(self: 'MenuItemSerializer', value: int):
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



    def update(
        self: 'MenuItemSerializer',
        instance: 'MenuItem',
        validated_data: {}) -> 'MenuItem':
        instance.title = validated_data.get('title', instance.title)
        instance.calories = validated_data.get('calories', instance.calories)
        instance.price = validated_data.get('price', instance.price)
        instance.image = validated_data.get('image', instance.image)
        instance.list_of_allergens = validated_data.get(
            'list_of_allergens',
            instance.list_of_allergens
        )
        instance.category = validated_data.get('category', instance.category)

        return instance

    def create(self: 'MenuItemSerializer', validated_data: {}) -> 'MenuItem':
        return MenuItem.items.create(**validated_data)
