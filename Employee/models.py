from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.TextField(null=True, blank=True)
    name=models.TextField(null=True,blank=True)
    dept = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    doj = models.DateField(null=True, blank=True)

    def __str__(self):
        if self.name:
            return self.name
        return "None"
