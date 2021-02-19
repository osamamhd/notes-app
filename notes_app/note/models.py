from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse


COLORS = (
    ('a', 'yellow'),
    ('b', 'red'),
    ('c', 'green'),
    ('d', 'blue'),
    ('e', 'indigo'),
    ('f', 'purple'),
    ('g', 'pink')
)

LABELS = (
    ('office', 'Office'),
    ('important', 'Important'),
    ('home', 'Home'),
    ('personal', 'Personal')
)

class Note(models.Model):
    title = models.CharField(max_length=220)
    content = models.TextField()
    slug = AutoSlugField("Note Titel", 
        unique=True, always_update=False, populate_from="title")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    color = models.CharField(max_length=1, choices=COLORS, default='a')
    label =models.CharField(max_length=20, choices=LABELS, default='home')

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note:detail', kwargs={"slug": self.slug})