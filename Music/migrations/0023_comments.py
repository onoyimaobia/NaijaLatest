# Generated by Django 2.0.3 on 2018-10-05 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0022_auto_20181001_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('name', models.CharField(max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('mixtape', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Music.Mixtape')),
            ],
        ),
    ]