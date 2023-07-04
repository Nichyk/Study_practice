from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title}'


class Notes(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=400)
    reminder = models.DateField('Дата нагадування')

    def __str__(self):
        return f'{self.title} {self.text} {self.reminder}'
