from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.CharField(max_length=12,null=False)
    ename = models.CharField(max_length=20,null=False)
    eemail = models.EmailField(null=False)
    econtact = models.CharField(max_length=15)
    class Meta:
        db_table="employee"