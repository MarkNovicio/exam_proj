# Generated by Django 2.2 on 2020-12-13 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes_app', '0002_auto_20201212_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotes',
            name='quote',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='quote_author',
            field=models.CharField(max_length=1000),
        ),
    ]
