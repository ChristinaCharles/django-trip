from django.db import models
from apps.login_app.models import User
from datetime import datetime


# Create your models here.
class TripManager(models.Manager):
    def trip_validator(self,postData):
        errors = {}
        today = datetime.today().strftime('%Y-%m-%d')
        if len(postData['dest']) < 4:
            errors['dest'] = 'Destination must be at least three characters long'
        if len(postData['start_date']) < 1:
            errors['start_date'] = 'Start date must be provided'
        if len(postData['end_date']) < 1:
            errors['end_date'] = 'End date must be provided'
        if len(postData['plan']) < 4:
            errors['plan'] = 'Plan must be at least three characters long'
        if postData['start_date'] > postData['end_date']:
            errors['date'] = 'Trip must begin before it ends!'
        if postData['start_date'] < today: 
            errors['too_early'] = 'Start date must be in the future'


        return errors

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    plan = models.TextField()
    user = models.ManyToManyField(User, related_name="users")
    created_by = models.ForeignKey(User, related_name='user_created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TripManager()
