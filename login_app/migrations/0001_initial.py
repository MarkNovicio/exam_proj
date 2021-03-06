# Generated by Django 2.2 on 2020-12-01 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=255)),
                ('birthday', models.DateField(blank=True)),
                ('password', models.CharField(max_length=255)),
                ('confirm_pw', models.CharField(max_length=255)),
            ],
        ),
    ]
