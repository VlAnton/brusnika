from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    title = models.CharField(null=True, max_length=100, unique=True)
    calories = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='static/media/images/', null=True, blank=True)
    allergens = models.ManyToManyField(
        'Allergens',
        related_name='menu_items',
    )
    category = models.ForeignKey(
        'Category',
        related_name='menu_items',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'
        order_with_respect_to = 'title'

    def __str__(self):
        return self.title


class Allergens(models.Model):
    title = models.CharField('Allergens', max_length=100)

    class Meta:
        verbose_name = 'Allergen'
        verbose_name_plural = 'Allergens'
        order_with_respect_to = 'title'

    def __str__(self):
        return self.title
