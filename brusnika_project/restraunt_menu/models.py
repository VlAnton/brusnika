from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    title = models.CharField(blank=False, null=False, max_length=100)
    calories = models.TextField(blank=False, null=False)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    list_of_allergens = models.OneToOneField('AllergensModel', on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )

    items = models.Manager

    class Meta:
        order_with_respect_to = 'title'

    def __str__(self):
        return self.title


class AllergensModel(models.Model):
    list_of_allergens = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.list_of_allergens
