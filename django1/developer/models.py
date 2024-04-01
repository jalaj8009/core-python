from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    developer_name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    project = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    submitting_date = models.DateField(max_length=50)
