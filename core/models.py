from django.db import models
from jsonfield import JSONField

class Channel(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, unique=True)
    language = models.CharField(max_length=2, null=False, blank=False)
    picture = models.ImageField(null=False, blank=False,upload_to="channels")
    parent_channel = models.ForeignKey('self',on_delete=models.CASCADE,related_name='subchannels',null=True,blank=True)

    def __str__(self):
        return self.title

class Content(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, unique=True)
    metadata = JSONField()
    channel = models.ForeignKey(Channel,on_delete=models.CASCADE,null=False)
    text = models.TextField(null=False, blank=False)
    rating = models.IntegerField()
    
    def __str__(self):
        return self.title

