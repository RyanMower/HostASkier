from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from localflavor.us.models import USStateField
from multiselectfield import MultiSelectField

WATERSKI_EVENTS =  ((1, 'Slalom'),
                    (2, 'Jump'),
                    (3, 'Trick'),
                    (3, 'Wake Surfing'),
                    (3, 'Wake Boarding'),
                    (4, 'Other'))

EVENTS =   ((1, 'Slalom'),
                    (2, 'Jump'),
                    (3, 'Trick'))


class Host(models.Model):

    name            = models.CharField(verbose_name="Name/Organization", max_length=254, null=False)
    email           = models.EmailField(verbose_name="Email", max_length=254, null=False)
    phone_number    = PhoneNumberField(verbose_name="Phone Number", null=False)
    address_1       = models.CharField(verbose_name="Address", max_length=128, null=False)
    address_2       = models.CharField(verbose_name="", max_length=128, blank=True, null=True)
    city            = models.CharField(verbose_name="City", max_length=128, null=False)
    state           = USStateField(verbose_name="State", null=False)
    zip_code        = models.CharField(verbose_name="Zip Code", max_length=5, null=False) 
    events          = MultiSelectField(verbose_name="Events", choices=EVENTS)
    availability    = models.TextField(verbose_name="Availability", null=True) 
    notes           = models.TextField(verbose_name="Additional Notes", null=True, blank=True)
    start_date      = models.DateField(verbose_name="Start Date")
    end_date        = models.DateField(verbose_name="End Date")
    image           = models.ImageField(verbose_name="Site Picture", upload_to="media/site_pics", null=True, blank=True)
    approved        = models.BooleanField(default=False, blank=True)
