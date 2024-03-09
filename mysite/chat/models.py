
from django.contrib.auth.models import User
from django.db import models

from mainPage.models import Product

class Conversation(models.Model):
    item = models.ForeignKey(Product, related_name='chats', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='chats')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    
    def mark_as_read(self):
        self.is_read = True
        self.save()