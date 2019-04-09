from django.db import models

class Volunteer(models.Model):
    name = models.CharField(max_length=250, null=True)
    email = models.EmailField(max_length=70, blank=True)
    contact = models.CharField(max_length=250, null=True)
    address = models.CharField(max_length=250, null=True)
    pincode = models.IntegerField()
    age = models.IntegerField()
    institution = models.CharField(max_length=250, null=True)
    educational_background = models.CharField(max_length=250,null=True)
    contribution_time = models.CharField(max_length=250, null=True)
    why_join = models.CharField(max_length=1000, null=True)
    latitude = models.CharField(max_length=1000, null=True)
    longitude = models.CharField(max_length=1000, null=True)

    def __unicode__(self):
        return self.name

class Donater(models.Model):
    partnering_entity = models.CharField(max_length = 250,null=True)
    institution = models.CharField(max_length=250, null=True)
    name = models.CharField(max_length = 100 , null=True)
    contact = models.CharField(max_length = 250,null=True)
    email = models.EmailField(max_length=70, blank=True)
    designation = models.CharField(max_length = 250,null=True)
    address = models.CharField(max_length=250, null=True)
    pincode = models.IntegerField()
    additional = models.CharField(max_length=1000, null=True)
    latitude = models.CharField(max_length=1000, null=True)
    longitude = models.CharField(max_length=1000, null=True)

    def __unicode__(self):
        return self.name

