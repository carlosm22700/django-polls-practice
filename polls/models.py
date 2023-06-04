import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
# A model is the source of information about your data
# it contains the essential fields and behaviors of the data you're storing.
# Django follows DRY principles. the goal is to define your data model in one place and automatically derive from it.

'''
to update database:
1) change models in models.py
2) Run python manage.py makemigrations
3) Run python manage.py migrate
'''


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now()
    datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
