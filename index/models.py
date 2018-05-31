from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    created= models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    message = models.CharField(max_length=300, null=True)
    
    def __unicode__(self):
        return self.message

    def __str__(self):
        return self.message
        

