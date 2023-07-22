from django.db import models

# Create your models here.



class userdetail(models.Model):
    username= models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password= models.CharField(max_length=100)
    repeatPassword= models.CharField(max_length=100)
    
    

class roadissue(models.Model):
    issue= models.CharField(max_length=100)
    fname= models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    datedata= models.CharField(max_length=100)
    NID= models.CharField(max_length=100)
    phone= models.CharField(max_length=100)
    Gendar=models.CharField(max_length=100)
    province= models.CharField(max_length=100)
    district= models.CharField(max_length=100)
    sector= models.CharField(max_length=100)
    cells=models.CharField(max_length=100)
    village= models.CharField(max_length=100)
    Issuedetails= models.CharField(max_length=100)
    
    Leadervillage= models.CharField(max_length=100)
    leadercell=models.CharField(max_length=100)
    leadersector= models.CharField(max_length=100)
    leaderdidtrict= models.CharField(max_length=100)

    
    mainroad= models.CharField(max_length=100)
    lenght= models.CharField(max_length=100)
    relateddata= models.CharField(max_length=100)
    
    vlagename= models.CharField(max_length=100)
    cellname= models.CharField(max_length=100)
    secotname= models.CharField(max_length=100)
    
    phonecvilage= models.CharField(max_length=100)
    phoneCells= models.CharField(max_length=100)
    phoneSector= models.CharField(max_length=100)
    status= models.IntegerField()
   


