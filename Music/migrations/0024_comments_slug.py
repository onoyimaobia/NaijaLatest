# Generated by Django 2.0.3 on 2018-10-05 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0023_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='slug',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
