# Generated by Django 3.2.4 on 2021-06-10 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('trading_outpost', '0008_alter_my_card_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_card',
            name='profile',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
    ]
