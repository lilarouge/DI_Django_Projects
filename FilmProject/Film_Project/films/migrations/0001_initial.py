# Generated by Django 3.2.3 on 2021-06-02 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('release_date', models.DateTimeField(auto_now_add=True)),
                ('available_in_countries', models.ManyToManyField(to='films.Country')),
                ('category', models.ManyToManyField(to='films.Category')),
                ('created_in_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_in_country', to='films.country')),
                ('director', models.ManyToManyField(to='films.Director')),
            ],
        ),
    ]
