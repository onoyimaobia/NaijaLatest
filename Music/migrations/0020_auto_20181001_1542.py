# Generated by Django 2.0.3 on 2018-10-01 14:42

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0019_auto_20181001_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mixtape',
            name='tracks',
            field=ckeditor.fields.RichTextField(max_length=2000),
        ),
    ]
