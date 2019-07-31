from django.db import models
import datetime


class Post(models.Model):
    title = models.CharField(max_length=120)
    publish_date = models.DateField(default=datetime.date.today)
    content = models.CharField(max_length=500)
    author = models.CharField(max_length=24)

    def __str__(self):
        return self.title + ", " + self.content + ", " + self.author
