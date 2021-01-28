from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profiles', null=True, blank=True)
    nombre = models.CharField(null=True, blank=True, max_length=50)
    apellido = models.CharField(null=True, blank=True, max_length=50)
    fecha = models.DateField(null=True, blank=True)
    genero = models.CharField(null=True,blank=True,max_length=50)
    direcccion = models.TextField(null=True, blank=True)
    

    class Meta:
        ordering = ['user__username']

class Profilephoto(models.Model):
    id_photo = models.IntegerField(primary_key=True)
    picture_location = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profilephoto'


""" Conflicto authUser """
# class RegistrationProfile(models.Model):
#     avatar = models.CharField(max_length=100, blank=True, null=True)
#     nombre = models.CharField(max_length=50, blank=True, null=True)
#     apellido = models.CharField(max_length=50, blank=True, null=True)
#     fecha = models.DateField(blank=True, null=True)
#     direcccion = models.TextField(blank=True, null=True)
#     user = models.OneToOneField(AuthUser, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'registration_profile'       