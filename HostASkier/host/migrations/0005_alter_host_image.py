# Generated by Django 3.2.4 on 2021-06-24 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0004_alter_host_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='./media/site_pics/', verbose_name='Site Picture'),
        ),
    ]
