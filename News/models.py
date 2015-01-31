from django.db import models

class News(models.Model):
   title = models.CharField(max_length=100)
   summary = models.CharField(max_length=500)
   picture = models.URLField(max_length=200)
   article = models.URLField(max_length=200)


