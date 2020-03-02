from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Hostel(models.Model):
    hostel=models.CharField(max_length=5)

    def __str__(self):
        return self.hostel

class Problem(models.Model):
    problem=models.CharField(max_length=20)

    def __str__(self):
        return self.problem

class Post(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    roll=models.CharField(max_length=10,null=False,blank=False)
    phone=models.PositiveIntegerField(max_length=10,null=False,blank=False)
    hall=models.ForeignKey(Hostel,on_delete=models.CASCADE)
    room=models.CharField(max_length=5,null=False,blank=False)
    issue=models.ForeignKey(Problem,on_delete=models.CASCADE)
    description=models.TextField()
    create_date=models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.roll

