from rest_framework import serializers

from .models import MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

    def create(self, validated_data):
        # title = validated_data.get('title' ,'')
        # calories = validated_data.get('calories' ,'')
        # price = validated_data.get('price' ,'')
        # image = validated_data.get('image' ,'')

        # item = MenuItem.items.create(**validated_data)
        # item.save()
        # print(validated_data)
        print(validated_data)
        return MenuItem.items.create(**validated_data)
        # return item

