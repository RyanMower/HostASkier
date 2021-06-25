# Generated by Django 3.2.4 on 2021-06-25 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0008_auto_20210625_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='./site_pics/', verbose_name='Site Picture 1'),
        ),
        migrations.AlterField(
            model_name='host',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='./site_pics/', verbose_name='Site Picture 2'),
        ),
        migrations.AlterField(
            model_name='host',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='./site_pics/', verbose_name='Site Picture 3'),
        ),
    ]
