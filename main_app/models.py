from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    page_count = models.IntegerField()

    def __str__(self):
        return "{} by {}, {} pages.".format(self.title, self.author, self.page_count)

class Pizza (models.Model):
    name = models.CharField(max_length=100)
    pizza_type = models.CharField(max_length=100)
    weight = models.IntegerField(help_text="grame")
    size = models.IntegerField (help_text="cm")

