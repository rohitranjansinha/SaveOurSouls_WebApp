from django.db import models

# Create your models here.
class Sample(models.Model):
    test = models.CharField(max_length=100)


class User_Base(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=1000)
    email = models.EmailField()

class Hospital_Base(models.Model):
    hospital_name = models.CharField(max_length=200)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    website = models.CharField(max_length=150)

class Hospital_Location(models.Model):
    username = models.CharField(max_length=100)
    hospital_lat = models.CharField(max_length=1000)
    hospital_lon = models.CharField(max_length=1000)

class Hospital_Wards(models.Model):
    username = models.CharField(max_length=100)
    emer_w = models.IntegerField()
    cardio_w = models.IntegerField()
    neuro_w = models.IntegerField()
    ortho_w = models.IntegerField()
    gen_w = models.IntegerField()

class Hospital_OPD(models.Model):
    username = models.CharField(max_length=100)
    cardio_t1 = models.CharField(max_length=10)
    cardio_t2 = models.CharField(max_length=10)
    neuro_t1 = models.CharField(max_length=10)
    neuro_t2 = models.CharField(max_length=10)
    ortho_t1 = models.CharField(max_length=10)
    ortho_t2 = models.CharField(max_length=10)
    dent_t1 = models.CharField(max_length=10)
    dent_t2 = models.CharField(max_length=10)
    gen_t1 = models.CharField(max_length=10)
    gen_t2 = models.CharField(max_length=10)

class Results(models.Model):
    username_user = models.CharField(max_length=100)    #User's username
    username_hospital = models.CharField(max_length=100)  #Hospital's Useernameß
    name = models.CharField(max_length=100,null=True)       #Hospital's Name
    website = models.CharField(max_length=150,null=True)    #Hospital's Website
    beds = models.IntegerField(null=True)
    location = models.CharField(max_length=1000,null=True)
    distance = models.DecimalField(null=True, max_digits=100,decimal_places=100)
    time = models.DecimalField(null=True, max_digits=100,decimal_places=100)
    opd1 = models.CharField(max_length=10,null=True)
    opd2 = models.CharField(max_length=10,null=True)


