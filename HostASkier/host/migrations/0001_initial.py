# Generated by Django 3.2.4 on 2021-06-20 21:21

from django.db import migrations, models
import localflavor.us.models
import multiselectfield.db.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='Name/Organization')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone Number')),
                ('address_1', models.CharField(max_length=128, verbose_name='Address')),
                ('address_2', models.CharField(blank=True, max_length=128, null=True, verbose_name='')),
                ('city', models.CharField(max_length=128, verbose_name='City')),
                ('state', localflavor.us.models.USStateField(max_length=2, verbose_name='State')),
                ('zip_code', models.CharField(max_length=5, verbose_name='Zip Code')),
                ('events', multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Slalom'), (2, 'Jump'), (3, 'Trick')], max_length=5, verbose_name='Events')),
                ('availability', models.TextField(null=True, verbose_name='Availability')),
                ('notes', models.TextField(null=True, verbose_name='Additional Notes')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('image', models.ImageField(null=True, upload_to='media/site_pics', verbose_name='Site Picture')),
                ('approved', models.BooleanField(blank=True, default=False)),
            ],
        ),
    ]
