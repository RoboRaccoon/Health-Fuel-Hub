# Generated by Django 5.0 on 2024-03-20 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HFH_app', '0008_rename_foodseaten_foodseaten_foodeaten'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FoodsEaten',
            new_name='FoodsEatenList',
        ),
    ]