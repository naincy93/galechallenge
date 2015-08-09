from django.db import models

# Create your models here.


# class newsletter(models.Model):
class ARTICLES(models.Model):
    class Meta:
        db_table = "ARTICLES"
        app_label = ""
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    hero = models.CharField(max_length=300)
    body = models.CharField(max_length=3000)
    pubdate = models.DateTimeField()
