# Generated by Django 3.2.4 on 2021-06-25 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0009_auto_20210625_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='name',
            field=models.CharField(max_length=254, verbose_name='Full Name'),
        ),
    ]
