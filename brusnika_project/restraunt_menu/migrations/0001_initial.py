# Generated by Django 2.2.3 on 2019-07-16 16:53

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_of_allergens', models.TextField(blank=True, null=True)),
            ],
            managers=[
                ('allergens', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
            managers=[
                ('categories', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('calories', models.TextField(blank=True, null=True)),
                ('price', models.PositiveIntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/media/images/')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='restraunt_menu.Category')),
                ('list_of_allergens', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='restraunt_menu.Allergens')),
            ],
            options={
                'order_with_respect_to': 'title',
            },
            managers=[
                ('items', django.db.models.manager.Manager()),
            ],
        ),
    ]
