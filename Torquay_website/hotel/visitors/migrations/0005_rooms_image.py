# Generated by Django 3.2.4 on 2021-06-05 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0004_remove_rooms_avaliable'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='image',
            field=models.ImageField(null=True, upload_to='upload/'),
        ),
    ]