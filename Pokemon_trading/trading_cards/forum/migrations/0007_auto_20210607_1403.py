# Generated by Django 3.2.4 on 2021-06-07 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('forum', '0006_auto_20210607_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='discussion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.discussion'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='forum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.forum'),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
        migrations.AlterField(
            model_name='forum',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
    ]
