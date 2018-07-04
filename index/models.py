from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    created= models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,)
    message = models.CharField(max_length=300, null=True)
    
    def __unicode__(self):
        return self.message

    def __str__(self):
        return self.message

class Dialog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user1 = models.ForeignKey(User,on_delete=models.DO_NOTHING,)
    user2 = models.CharField(max_length=300, default="toComputer")
    dialogue = models.CharField(max_length=300, null=True)
    
    def __unicode__(self):
        return self.dialogue
    
    def __str__(self):
        return self.dialogue
        
class Number(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,)
    number= models.IntegerField()
    
    def __unicode__(self):
        return self.number
    
    def __str__(self):
        return str(self.number)
