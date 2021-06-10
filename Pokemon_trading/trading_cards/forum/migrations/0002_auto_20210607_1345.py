# Generated by Django 3.2.4 on 2021-06-07 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forum',
            old_name='description',
            new_name='comment',
        ),
        migrations.RemoveField(
            model_name='forum',
            name='email',
        ),
        migrations.RemoveField(
            model_name='forum',
            name='link',
        ),
        migrations.AlterField(
            model_name='forum',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
    ]