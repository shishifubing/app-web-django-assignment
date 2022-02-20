from django.db import models

# Create your models here.


class Article(models.Model):
    name = models.CharField(max_length=50, unique=True)
    article_text = models.TextField()
    publication_date = models.TimeField()

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'
