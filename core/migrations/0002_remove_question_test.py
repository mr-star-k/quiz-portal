# Generated by Django 2.0.6 on 2018-06-13 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='test',
        ),
    ]
