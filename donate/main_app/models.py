from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    donor = models.BooleanField(default=None, blank=True, null=True)
    company = models.BooleanField(default=None, blank=True, null=True) 

# Create your models here.
Type = (
    ('P', 'Plastic'),
    ('p', 'Paper'),
    ('G', 'Glass Bottles'),
    ('c', 'Containers')
) 

class Donate(models.Model):
    item_name = models.CharField('Name', max_length=100)
    #    date = models.DateField('Pick up date')
    # date = models.CharField('Pick up Date', max_length=100)
    date = models.DateField('Pick up Date', max_length=100)
    time = models.TimeField('Pick up Time', max_length=100)
    #    time = models.TimeField('Pick up time')
    location =  models.CharField('Pick up Location', max_length=100) 
    #    location =  models.SpatialLocationField() 
    num = models.IntegerField('Number', default=0)
    typeofDonate = models.CharField('Type',
        max_length=1,
        choices=Type,
        default=Type[0][0]
                                    )
  # Add the foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.item_name

