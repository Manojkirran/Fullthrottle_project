from django.db import models

class members(models.Model):
     Emp_id = models.CharField(max_length=15)
     real_name = models.CharField(max_length=15)
     tz = models.CharField(max_length=25)
     activity_periods = models.CharField(max_length=1000)

     def __str__(self):
         return self.Emp_id
