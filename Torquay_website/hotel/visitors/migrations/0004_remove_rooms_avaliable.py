# Generated by Django 3.2.4 on 2021-06-04 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0003_contactform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rooms',
            name='avaliable',
        ),
    ]