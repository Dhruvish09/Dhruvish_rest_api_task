import email
from pyexpat import model
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser)

class UserManager(BaseUserManager):
  def create_user(self, email, name,phone_number,dob ,password=None, password2=None):
      """
      Creates and saves a User with the given email, name and password.
      """
      if not email:
          raise ValueError('User must have an email address')

      user = self.model(
          email=self.normalize_email(email),
          name=name,
          phone_number=phone_number,
          dob=dob
          
      )

      user.set_password(password)
      
      user.save(using=self._db)
      return user

  def create_superuser(self, email, name,phone_number,dob, password=None):
      """
      Creates and saves a superuser with the given email, name and password.
      """
      user = self.create_user(
          email,
          
          name=name,
          phone_number=phone_number,
          dob=dob,
          password=password,
          
      )
      user.is_admin = True
      user.save(using=self._db)
      return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email',max_length=255,unique=True)
    name = models.CharField(max_length=200)
    phone_number= models.IntegerField()
    dob = models.DateField(null= True)
    profile_image = models.ImageField(upload_to='media',default="default.jpg",null=True,blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','phone_number','dob']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
















  

