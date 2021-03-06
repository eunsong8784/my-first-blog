
from django.db import models
# Create your models here.
import datetime
from django.db import models
from django.utils import timezone

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return  now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, choices= [(1,'A'), (2,'B'), (3,'C'), (4,'D')])
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Answer(models.Model):
    ans_text = models.BooleanField()
    def __str__(self):
        return self.ans_text


