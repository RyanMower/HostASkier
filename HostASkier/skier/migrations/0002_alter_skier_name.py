# Generated by Django 3.2.4 on 2021-06-25 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skier', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skier',
            name='name',
            field=models.CharField(max_length=254, verbose_name='Full Name'),
        ),
    ]