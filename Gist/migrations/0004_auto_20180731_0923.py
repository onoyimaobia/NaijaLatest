# Generated by Django 2.0.3 on 2018-07-31 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gist', '0003_auto_20180730_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gistpost',
            name='slug',
            field=models.SlugField(max_length=300, unique=True),
        ),
    ]
