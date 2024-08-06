from django.db import models

# Create your models here.
class Reg(models.Model):
    name=models.CharField(max_length=20)
    dob=models.CharField(max_length=15)
    em=models.CharField(max_length=15)
    sap=models.CharField(max_length=15)
    ste=models.CharField(max_length=15)
    ad=models.IntegerField(primary_key=True)

class Apreg(models.Model):
    ad=models.IntegerField(primary_key=True)
    sap=models.CharField(max_length=15)

class Tsreg(models.Model):
    ad=models.IntegerField(primary_key=True)
    ste=models.CharField(max_length=15)

class Pollsap(models.Model):
	ad=models.IntegerField(primary_key=True)
	td=models.IntegerField()
	ys=models.IntegerField()
	no=models.IntegerField()

class Pollsts(models.Model):
	ad=models.IntegerField(primary_key=True)
	tr=models.IntegerField()
	co=models.IntegerField()
	bj=models.IntegerField()


