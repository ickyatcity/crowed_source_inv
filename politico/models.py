from django.db import models

# Create your models here.

class Candidate(models.Model):
    cadidate = models.CharField(max_length=225)
    cadidate_desc = models.CharField(max_length=225)
    url_wiki = models.CharField(max_length=255, blank=True, null=True)
    title_wiki = models.CharField(max_length=255, blank=True, null=True)
    content_wiki = models.TextField(blank=True, null=True)
