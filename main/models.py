from django.db import models

# Create your models here.
class Updates(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    included_in_client = models.BooleanField(default=False)
    update_link = models.URLField(blank=True)
    fix_link = models.URLField(blank=True)
    date = models.DateField(auto_now=True)
