from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse

class Note(models.Model):
    title = models.CharField(max_length=220)
    content = models.TextField()
    slug = AutoSlugField("Note Titel", 
        unique=True, always_update=False, populate_from="title")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note:detail', kwargs={"slug": self.slug})