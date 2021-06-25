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

# Create your models here.
class Skier(models.Model):

    name            = models.CharField(verbose_name="Name/Organization", max_length=254, null=False)
    email           = models.EmailField(verbose_name="Email", max_length=254, null=False)
    phone_number    = PhoneNumberField(verbose_name="Phone Number", null=False)
    city            = models.CharField(verbose_name="City", max_length=128, null=False)
    state           = USStateField(verbose_name="State", null=False)
    events          = MultiSelectField(verbose_name="Events", choices=EVENTS)
    availability    = models.TextField(verbose_name="Availability", null=True)
    start_date      = models.DateField(verbose_name="Start Date")
    end_date        = models.DateField(verbose_name="End Date")
    university      = models.CharField(verbose_name="Universtiy Affiliation (if applicable)", max_length=254, blank=True, null=True)
    approved        = models.BooleanField(default=False, blank=True)