# Generated by Django 2.2 on 2020-12-16 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0004_remove_registration_birthday'),
        ('quotes_app', '0004_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotes',
            name='favorites',
            field=models.ManyToManyField(related_name='favorite_quotes', to='login_app.Registration'),
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]
