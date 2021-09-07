from django.db import models

# Class Question inherits from models.Model
class Question(models.Model):
    # Id is auto-generated and auto-incremented
    # This will hold the question
    question_text = models.CharField(max_length=200)
    # Publication date
    pub_date = models.DateTimeField('date published')
    # defining the to string method, returns the question text
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # ForeignKey is a relationship between two models, (cascade = because if the question is deleted, the choices are too)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # This will the Choice text
    choice_text = models.CharField(max_length=200)
    # This will be the votes count
    votes = models.IntegerField(default=0)
    # defing the to string method, returns the choice text
    def __str__(self):
        return self.choice_text
