from django.db import models

# Create your models here.
class menu(models.Model):
    img=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name