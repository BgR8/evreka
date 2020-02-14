# Generated by Django 2.1.7 on 2020-02-13 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Navigation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Tarih')),
                ('latitude', models.FloatField(max_length=120, verbose_name='Enlem')),
                ('longitude', models.FloatField(max_length=120, verbose_name='Boylam')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.CharField(max_length=200, verbose_name='Plaka')),
            ],
        ),
    ]
