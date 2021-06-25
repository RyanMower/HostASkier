from django.db import models


# Create your models here.
class HomeText(models.Model):
    Home_Text = models.TextField(verbose_name="Text on front page of website.")
