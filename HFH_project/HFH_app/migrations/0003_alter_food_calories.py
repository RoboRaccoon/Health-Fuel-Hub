# Generated by Django 5.0 on 2024-03-18 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HFH_app', '0002_alter_food_calories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='calories',
            field=models.IntegerField(default=0),
        ),
    ]
