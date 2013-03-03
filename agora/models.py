from django.db import models
from graph.models import Taggable
from datetime import datetime

class Thread(Taggable):
    """Discussion"""
    pass

class Message(models.Model):
    thread = models.ForeignKey(Thread)
    index = models.IntegerField()
    posted = models.DateTimeField(auto_now=True)
    text = models.TextField()
    
    def reply(klass, thread, text):
        msg = klass()
        msg.thread = thread
        msg.posted = datetime.today()
        msg.text = text
        msg.index = klass.objects.filter(thread=thread).count()
        msg.save()
    
    reply = classmethod(reply)
    
    def to_dict(self):
        return {'index':self.index, 'posted':str(self.posted), 'text':str(self.text)}
