from django.db import models
from graph.models import Taggable
from datetime import datetime

class Thread(Taggable):
    """Discussion"""
    class CannotHaveChildren(Exception):
        def __init__(self):
            Exception.__init__(self, 'For now, Thread objects could only be leafs in the graph')


    def attach(self, other,*args,**kwargs):
        raise self.CannotHaveChildren


    def reply(self, **kwargs):
        """Automatically replies to a Thread"""
        kwargs['index'] = Message.objects.filter(thread=self).count()
        kwargs['thread'] = self
        kwargs['posted'] = datetime.today()
        msg = Message.objects.create(**kwargs)
        msg.save()


class Message(models.Model):
    thread = models.ForeignKey(Thread)
    index = models.IntegerField()
    posted = models.DateTimeField(auto_now=True)
    text = models.TextField()

    def to_dict(self):
        return {'index':self.index, 'posted':str(self.posted), 'text':str(self.text)}

from django import forms

# class MessageForm(forms.ModelForm):
#     class Meta:
#         model = Message

class TreadForm(forms.Form):
    subject = forms.CharField(max_length=100)
    tags = forms.CharField()

class MessageForm(forms.Form):
    text = forms.CharField()