# Generated by Django 2.2.3 on 2019-07-10 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restraunt_menu', '0002_auto_20190709_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='restraunt_menu.Category'),
        ),
    ]