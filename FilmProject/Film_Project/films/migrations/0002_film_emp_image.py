# Generated by Django 3.2.3 on 2021-06-02 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='emp_image',
            field=models.ImageField(null=True, upload_to='upload/'),
        ),
    ]
