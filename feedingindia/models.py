from django.db import models
from django.contrib.auth.models import User

class Volunteer(models.Model):
    name = models.CharField(max_length=250, null=True)
    email = models.EmailField(max_length=70, blank=True, null=True)
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
    email = models.EmailField(max_length=70, blank=True, null=True)
    designation = models.CharField(max_length = 250,null=True)
    address = models.CharField(max_length=250, null=True)
    pincode = models.IntegerField()
    additional = models.CharField(max_length=1000, null=True)
    latitude = models.CharField(max_length=1000, null=True)
    longitude = models.CharField(max_length=1000, null=True)

    def __unicode__(self):
        return self.name

class Shelter(models.Model):
    name_hunger_spot = models.CharField(max_length = 100 , null=True)
    address = models.CharField(max_length = 250,null=True)
    pincode = models.IntegerField()
    total_benefitiaries = models.IntegerField()
    type_shelter = models.CharField(max_length = 100 , null=True)
    raw_food = models.CharField(max_length = 250,null=True)
    cooked_food = models.CharField(max_length = 250,null=True)
    preference = models.CharField(max_length = 250,null=True)
    time_range = models.CharField(max_length = 250,null=True)
    heat_food = models.CharField(max_length = 250,null=True)
    refrigerate_food = models.CharField(max_length = 250,null=True)
    external_support = models.CharField(max_length = 250,null=True)
    support = models.CharField(max_length = 250,null=True)
    reg_status = models.CharField(max_length = 250,null=True)
    name_incharge = models.CharField(max_length = 250,null=True)
    contact_incharge = models.CharField(max_length = 250, null=True)
    email_incharge = models.EmailField(max_length=70, blank=True,null=True)
    latitude = models.CharField(max_length=1000, null=True)
    longitude = models.CharField(max_length=1000, null=True)
    
    def __unicode__(self):
        return self.name


class Donation(models.Model):
    name = models.CharField(max_length=250, null=True)
    contact = models.CharField(max_length=250, null=True)
    address = models.CharField(max_length=250, null=True)
    date_donate = models.CharField(max_length = 250,null=True)
    time_donate = models.CharField(max_length = 250,null=True)
    food_for_donate = models.IntegerField()
    counter = models.IntegerField()

    def __unicode__(self):
        return self.name


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

	# venue_address = models.CharField(max_length = 250,null=True)
 #    venue_pincode = models.CharField(max_length = 250,null=True)
 #    time = models.CharField(max_length = 250,null=True)
 #    request = models.CharField(max_length = 250,null=True)
 #    drop_off = models.CharField(max_length = 250,null=True)