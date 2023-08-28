from django.db import models

# Create your models here.
class district(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tourist_Spot = models.CharField(max_length=300)
    image = models.ImageField(upload_to="district_Images",blank=True,null=True)

class popular_Destination(models.Model):
    spot_Title = models.CharField(max_length=200)
    place_Title = models.CharField(max_length=100)
    description  = models.TextField()
    images = models.ImageField(upload_to="destination_Images",blank=True,null=True)

class packages(models.Model):
    title= models.CharField(max_length=200)
    place_Title = models.CharField(max_length=100,blank=True,null=True)
    image1 = models.ImageField(upload_to="package_Images",blank=True,null=True)
    image2 = models.ImageField(upload_to="package_Images",blank=True,null=True)
    image3 = models.ImageField(upload_to="package_Images",blank=True,null=True)
    image4 = models.ImageField(upload_to="package_Images",blank=True,null=True)
    image5 = models.ImageField(upload_to="package_Images",blank=True,null=True)
    ultimatePrice = models.IntegerField(blank=True,null=True)
    luxuryPrice = models.IntegerField(blank=True,null=True)
    budgetPrice = models.IntegerField(blank=True,null=True)
