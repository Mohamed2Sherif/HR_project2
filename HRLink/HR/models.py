from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError("Enter a Proper Email please >=(")
        if not username:
            raise ValueError("Enter a Proper Email please >=(")
        user = self.model(email=self.normalize_email(email),username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,    
    )
        user.is_admin=True
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):
    email       =models.EmailField(verbose_name="email", max_length=50,unique=True)
    accId       =models.IntegerField(default=0)
    username    =models.CharField(max_length=20 , unique=True)
    is_admin    =models.BooleanField(default=False)
    is_active   =models.BooleanField(default=True)
    is_staff    =models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    phone       =models.CharField(max_length=11, verbose_name="Phone_Number",null=True)
    DOB         =models.DateField(null=True)
    availableVac=models.IntegerField(default=0)
    approvedVac =models.IntegerField(default=0)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=['username',]
    
    objects = AccountManager()

    def __str__(self):
        return self.username

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True


class Employee(models.Model)  :

    email       =models.EmailField(verbose_name="email", max_length=50,unique=True)
    accId       =models.IntegerField(default=0)
    Name    =models.CharField(max_length=20)
    address    =models.CharField(max_length=500,null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    gender = models.CharField(max_length=1,null=True,choices=GENDER_CHOICES)
    salary      =models.FloatField(default=0,verbose_name="Salary")
    phone       =models.CharField(max_length=11, verbose_name="Phone_Number",null=True)
    Birth_date         =models.DateField(null=True)
    availableVac=models.IntegerField(default=0)
    approvedVac =models.IntegerField(default=0)