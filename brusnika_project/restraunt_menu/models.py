from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    categories = models.Manager()

    class Meta:
        verbose_name_plural = 'categories'
        app_label = 'restraunt_menu'

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    title = models.CharField(blank=False, null=False, max_length=100, unique=True)
    calories = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField(blank=False, null=False)
    image = models.ImageField(upload_to='static/media/images/', null=True, blank=True)
    list_of_allergens = models.ForeignKey(
        'Allergens',
        null=True,
        blank=True,
        unique=False,
        on_delete=models.SET_NULL
    )
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        unique=False,
        on_delete=models.SET_NULL
    )

    items = models.Manager()

    class Meta:
        order_with_respect_to = 'title'
        app_label = 'restraunt_menu'

    def __str__(self):
        return self.title


class Allergens(models.Model):
    list_of_allergens = models.TextField(blank=True, null=True)

    allergens = models.Manager()

    class Meta:
        app_label = 'restraunt_menu'

    def __str__(self):
        return self.list_of_allergens

