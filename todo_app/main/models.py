from django.db import models

# Create your models here.

class NavLink(models.Model):
    name =   models.CharField(verbose_name="name", max_length=50)


    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name