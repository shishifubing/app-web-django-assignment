from django.db.models import Model, CharField, TextField, DateTimeField

# Create your models here.


class Article(Model):
    name = CharField(max_length=50, unique=False)
    description = TextField()
    publication_date = DateTimeField(auto_now_add=True)
    author_name = CharField(
        max_length=50,
        unique=False,
        default='Anonymous',
        blank=False,
        null=False)

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'

    def get_absolute_url(self):
        return f'/news/{self.id}'
