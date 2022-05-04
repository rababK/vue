from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class post(models.Model):
    writer= models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=True)
    content = models.CharField( max_length=1500,blank=True)
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return str(self.created_at)
