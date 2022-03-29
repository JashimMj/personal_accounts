from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CompanyInformation(models.Model):
    id = models.AutoField(primary_key=True)
    Company_Name = models.CharField(max_length=500, null=True, blank=True)
    Company_Address = models.CharField(max_length=1000, null=True, blank=True)
    Company_Email = models.EmailField(max_length=50, null=True, blank=True)
    Company_Phone = models.CharField(max_length=50, null=True, blank=True)
    Company_Fax = models.CharField(max_length=50, null=True, blank=True)
    Company_Web_site = models.CharField(max_length=50, null=True, blank=True)
    Company_Short_Name = models.CharField(max_length=50, null=True, blank=True)
    create_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    logo = models.ImageField(upload_to='logo', null=True, blank=True)
    Edits = models.CharField(max_length=10, null=True, blank=True)
    objects = models.Manager()

    def image(self):
        try:
            urls = self.logo.url
        except:
            urls = ''
        return urls

    def __str__(self):
        return self.Company_Name


class CashReceiveList(models.Model):
    id = models.AutoField(primary_key=True)
    Name=models.CharField(max_length=500, null=True, blank=True)
    datess = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    objects = models.Manager()
    def __str__(self):
        return self.Name

class CashReceiveEntry(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.ForeignKey(CashReceiveList,on_delete=models.CASCADE,null=True,blank=True)
    Amount=models.FloatField()
    Narration=models.TextField(max_length=500, null=True, blank=True)
    datess = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    To_Date = models.DateField(null=True, blank=True)
    objects = models.Manager()
    def __str__(self):
        return self.Name.Name



class ExpenseList(models.Model):
    id = models.AutoField(primary_key=True)
    Name=models.CharField(max_length=500, null=True, blank=True)
    datess = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    objects = models.Manager()
    def __str__(self):
        return self.Name


class ExpenseEntry(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.ForeignKey(ExpenseList,on_delete=models.CASCADE,null=True,blank=True)
    Amount=models.FloatField()
    Narration=models.TextField(max_length=500, null=True, blank=True)
    datess = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    To_Date = models.DateField(null=True, blank=True)
    objects = models.Manager()
    def __str__(self):
        return self.Name.Name




