from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    donor = models.BooleanField(default=None, blank=True, null=True)
    company = models.BooleanField(default=None, blank=True, null=True) 

# Create your models here.
Type = (
    ('Plastic','Plastic'),
    ('Paper','Paper'),
    ('Glass Bottles','Glass Bottles'),
    ('Containers','Containers')
) 

class Donate(models.Model):
    item_name = models.CharField('Name', max_length=100)
    #    date = models.DateField('Pick up date')
    # date = models.CharField('Pick up Date', max_length=100)
    item_image = models.TextField('Item Image', max_length=350)
    date = models.DateField('Pick up Date', max_length=100)
    time = models.TimeField('Pick up Time', max_length=100)
    #    time = models.TimeField('Pick up time')
    location =  models.CharField('Pick up Location', max_length=100) 
    #    location =  models.SpatialLocationField() 
    status = models.BooleanField('Availability', default = True)
    num = models.IntegerField('Number', default=0)
    typeofDonate = models.CharField('Type',
        max_length=100,
        choices=Type,
        default=Type[0][0]
                                    )
  # Add the foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.item_name
    def get_absolute_url(self):
        return reverse('detail', kwargs={'Donate_id': self.id})


class Photo(models.Model):
  url = models.CharField(max_length=200)
  Donate = models.ForeignKey(Donate, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for Donate_id: {self.Donate_id} @{self.url}"
