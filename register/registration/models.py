from django.db import models

# Create your models here.
class Profile1(models.Model):
   name = models.CharField(max_length = 100)
   lastName = models.CharField(max_length = 100)
   password = models.CharField(max_length = 100)
  # picture = models.ImageField(upload_to = '/home/harsh/Desktop/Registration/register')

   class Meta:
      db_table = "profile1"