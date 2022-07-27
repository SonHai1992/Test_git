from django.db import models


# Create your models here.
from nltk.sem.chat80 import country


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    date_time = models.DateTimeField('Time')
    delete = models.BooleanField(default=False)

    def __str__(self):
        return self.question_text
    class Meta:
        ordering = ('id',)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Customer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=3)