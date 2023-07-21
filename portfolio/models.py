from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

# from django.db.models.fields.related import ForeignKey


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to="portfolio/images/")
    url = models.URLField(blank=True)
    # url = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.title
