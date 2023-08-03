# imports: models and date/time
from django.db import models
from django.utils import timezone
import datetime

# models created below

# question model which contains the question text and its publication date
class Question(models.Model):
    question_text = models.CharField(max_length=200)    # question attribute
    pub_date = models.DateTimeField("date published")   # publication date attribute

    
    def __str__(self):  # define a tostring for readability
        return self.question_text
    
    # returns true if the publication date was within 1 day of the current time
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



# choice model which contains the choice text and its vote tally; question foreign key
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
