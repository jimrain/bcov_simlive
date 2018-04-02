from django.db import models
from django_mysql.models import ListTextField


class BCAccount(models.Model):
   name = models.CharField(max_length=200)
   accountId = models.CharField(max_length=200)
   clientId = models.CharField(max_length=200)
   clientSecret = models.CharField(max_length=200)
   liveAccountId = models.CharField(max_length=200, null=True, blank=True)
   liveApiToken = models.CharField(max_length=200, null=True, blank=True)
   liveClippingCreds = models.CharField(max_length=200, null=True, blank=True)

   def __str__(self):
       return self.name


class Channel(models.Model):
    name = models.CharField(max_length=200)
    bcAccount = models.ForeignKey(BCAccount, on_delete=models.DO_NOTHING,)
    start_time = models.DateTimeField()
    content_dir = models.CharField(max_length=200)
    smil_file = models.CharField(max_length=200)
    ProgramBlockList =  ListTextField(
        base_field=models.IntegerField(),
        size=20,
    )

    def __str__(self):
        return self.name


class ProgramBlock(models.Model):
    name = models.CharField(max_length=200)
    duration = models.IntegerField()
    DayBlockList =  ListTextField(
        base_field=models.IntegerField(),
        size=20,
    )

    def __str__(self):
        return self.name

class DayBlock(models.Model):
    name = models.CharField(max_length=200)
    duration = models.IntegerField()
    VideoList =  ListTextField(
        base_field=models.IntegerField(),
        size=20,
    )

    def __str__(self):
        return self.name

class Video(models.Model):
    title = models.CharField(max_length=200)
    bcAccount = models.ForeignKey(BCAccount, on_delete=models.DO_NOTHING,)
    video_id = models.CharField(max_length=20) # From video cloud
    duration = models.IntegerField()
    description = models.TextField()
    path = models.CharField(max_length=200) # File system path to video.

    def __str__(self):
        return self.title
