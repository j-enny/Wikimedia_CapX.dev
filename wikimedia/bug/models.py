
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
    
    
    description = models.CharField(max_length=200)
    bug_type = models.CharField(max_length=20, choices=bug_type)
    report_date = models.DateTimeField()
    status = models.CharField(max_length=25, choices=status)
    
    def __str__(self):
        return self.description