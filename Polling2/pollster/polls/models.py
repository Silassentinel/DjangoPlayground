from django.db import models

class Question(models.Model):
    # Question_text which is the question itself
    question_text = models.CharField(max_length=200)
    # pub_date is the date the question was published
    pub_date = models.DateTimeField('date published')
    # defining string method which returns the question text
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # ForeignKey for a relation between Question and Choice 
    # #with cascade because if there is no question there is no reason to it's have choices
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Choice_text which is the choice itself
    choice_text = models.CharField(max_length=200)
    # votes is the number of votes the choice has
    votes = models.IntegerField(default=0)
    # defining string method which returns the choice text
    def __str__(self):
        return self.choice_text
