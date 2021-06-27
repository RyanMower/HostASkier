from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from localflavor.us.models import USStateField
from multiselectfield import MultiSelectField
from PIL import Image
from django.core.validators import RegexValidator


zip_validator = RegexValidator(r"^[0-9]{5}(?:-[0-9]{4})?$", "Sorry, please enter a valid zip code.")

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

    name            = models.CharField(verbose_name="Full Name", max_length=254, null=False)
    email           = models.EmailField(verbose_name="Email", max_length=254, null=False)
    phone_number    = PhoneNumberField(verbose_name="Phone Number", null=False)
    address_1       = models.CharField(verbose_name="Address", max_length=128, null=False)
    address_2       = models.CharField(verbose_name="", max_length=128, blank=True, null=True)
    city            = models.CharField(verbose_name="City", max_length=128, null=False)
    state           = USStateField(verbose_name="State", null=False)
    zip_code        = models.CharField(verbose_name="Zip Code", max_length=10, null=False, validators=[zip_validator]) 
    events          = MultiSelectField(verbose_name="Events", choices=EVENTS)
    availability    = models.TextField(verbose_name="Availability", null=True) 
    notes           = models.TextField(verbose_name="Additional Notes", null=True, blank=True)
    start_date      = models.DateField(verbose_name="Start Date")
    end_date        = models.DateField(verbose_name="End Date")
    image1          = models.ImageField(verbose_name="Site Picture 1", upload_to="./site_pics/", null=True, blank=True)
    image2          = models.ImageField(verbose_name="Site Picture 2", upload_to="./site_pics/", null=True, blank=True)
    image3          = models.ImageField(verbose_name="Site Picture 3", upload_to="./site_pics/", null=True, blank=True)
    approved        = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f'Host: {self.email}'

    def save(self, *args, **kwargs):
        # save parent class 
        super().save(*args, **kwargs)
        
        # Save and resize Host images
        raw_images = [self.image1, self.image2, self.image3] ## Makes sure an image was supplied
        images = []
        for img in raw_images:
            if img:
                images.append(img)

        for image in images:
            img = Image.open(image.path)
            if img.height > 300 or img.width > 300: # Resize with correct scale
                width_bigger = True
                if img.height > img.width:  # Find which side is bigger
                    width_bigger = False

                delta = None ## Initializing values here
                scale = None
                if width_bigger:
                    delta = img.width - 300
                    scale = 1 - (delta / img.width)
                else:
                    delta = img.height - 300
                    scale = 1 - (delta / img.height)
                
                new_width = img.width * scale
                new_height = img.height * scale

                output_size = (new_width,new_height)
                img.thumbnail(output_size)
                img.save(image.path) 
