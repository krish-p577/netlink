from django.db import models
from django.conf import settings
# Create your models here.
class Linkset(models.Model):
    biography = models.CharField(max_length=300, null = True)
    linkone = models.CharField(max_length=300, null = True)
    defone = models.CharField(max_length=300)
    linktwo = models.CharField(max_length=300, null = True)
    deftwo = models.CharField(max_length=300)
    linkthree = models.CharField(max_length=300, null = True)
    defthree = models.CharField(max_length=300)
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        blank = True,
        null = True)


    



