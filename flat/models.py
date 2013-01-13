from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()

    """ 
    a flat corresponds with an IS24 expose_id
    """

class Flat(models.Model):
	expose_id = models.CharField(max_length=10)
	title = models.CharField(max_length=20)
	
