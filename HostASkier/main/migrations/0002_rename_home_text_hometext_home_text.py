# Generated by Django 3.2.4 on 2021-06-25 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hometext',
            old_name='home_text',
            new_name='Home_Text',
        ),
    ]
