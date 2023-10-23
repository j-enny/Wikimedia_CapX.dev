
from django.db import models

# Create your models here.
class Bug(models.Model):
    
    bug_type= (
        ('error','Error'),
                 ('new','New Feature'),
                 ('update','Update Needed')
    )
    
    status = (('to do','To Do'),
              ('in progress','In Progress'),
              ('done','Done')
              )
    
    
    description = models.CharField(name="Description", max_length=200)
    bug_type = models.CharField(name="Type", max_length=50, choices=bug_type)
    report_date = models.DateTimeField(name="Date Registered")
    status = models.CharField(name="Status", max_length=20, choices=status)
    
    def __str__(self):
        return self.description