from django.db import models
from django.utils import timezone

# Create your models here.
class FeedBack(models.Model):
    email=models.CharField(max_length=45,primary_key=True)
    name=models.CharField(max_length=55,null=False)
    rating=models.CharField(max_length=5,null=False)
    remark=models.TextField(default="")
    user_pic=models.CharField(max_length=255,default="")
    date=models.DateField(default=timezone.now)
    def _str_(self):#it represent object into string form#self means object
        return self.name
##contact table model###
class Contact(models.Model):
    email=models.CharField(max_length=45,null=False)
    name=models.CharField(max_length=55,null=False)
    phone=models.CharField(max_length=13,null=False)
    question=models.TextField()
    date=models.DateField(default=timezone.now)
    def _str_(self):#it represent object into string form#self means object
        return self.name
    ##registration model#
class User(models.Model):
     name=models.CharField(max_length=45)
     email=models.EmailField(max_length=45,primary_key=True)
     password=models.CharField(max_length=45)
     phone=models.CharField(max_length=13)
     profile_pic=models.FileField(upload_to="user_pic/",default="")
     date=models.DateField(default=timezone.now)
     def _str_(self):#it represent object into string form#self means object
        return self.name
     ##owner
class Owner(models.Model):
     name=models.CharField(max_length=45)
     email=models.CharField(max_length=45,primary_key=True)
     password=models.CharField(max_length=45,null=False)
     phone=models.CharField(max_length=13,null=False)
     city=models.CharField(max_length=50,null=False)
     address=models.CharField(max_length=45,null=False)
     profile_pic=models.FileField(upload_to="user_pic/",default="")
     date=models.DateField(default=timezone.now)
     def _str_(self):#it represent object into string form#self means object
        return self.name
     ##owner
class OwnerLogin(models.Model):
    email=models.CharField(max_length=45)
    password=models.CharField(max_length=30)
    date=models.DateField(default=timezone.now)
    def _str_(self):
        return self.email 
    

class Product(models.Model):
    owner=models.ForeignKey(Owner,on_delete=models.DO_NOTHING)
    product_name=models.CharField(max_length=30,null=False)
    product_category=models.CharField(max_length=40,null=False)
    product_description=models.TextField()
    product_price=models.CharField(max_length=10,null=False) 
    product_pic=models.FileField(upload_to="product_pic/",default="")
    product_status=models.CharField(default="available")


class Inventory(models.Model):
    user_phone = models.CharField(max_length=13)
    product_id = models.CharField(max_length=10,primary_key=True)
    owner_email = models.EmailField(max_length=255)
    duration = models.CharField(max_length=50)
    returndate = models.CharField(max_length=10, null=True, blank=True)
    id_proof = models.FileField(upload_to="id_proof/", default="")
    product_status = models.CharField(max_length=50,default="rented")
    rented_date = models.DateTimeField(default=timezone.now)