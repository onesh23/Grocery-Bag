from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
# Create your models here.

STATUS_CHOICES = (
    ('BOUGHT','Bought'),
    ('PENDING','Pending'),
    ('NOT AVAILABLE','Not Available')
)


class Item(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='PENDING')
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    date = models.DateField(default=datetime.now)
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name