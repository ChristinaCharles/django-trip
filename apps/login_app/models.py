from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        usr = User.objects.filter(email=postData['email'])
        if len(usr) > 0: 
            errors['unique_email'] = 'Email already exists. Please login.'
        if len(postData['fname']) < 3: 
            errors['first_name'] = 'First name should be longer than two characters'
        if len(postData['lname']) < 3: 
            errors['last_name'] = 'Last name should be longer than two characters'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Enter a valid email address'
        if postData['password'] != postData['pconfirm']:
            errors['password'] = 'Passwords do not match'
        if len(postData['password']) < 8:
            errors['pword_length'] = 'Password must be at least 8 characters long'
        return errors
    
    def login_validator(self, postData):
        errors = {}
        user = User.objects.get(email=postData['loginEmail'])

        if not User.objects.get(email=postData['loginEmail']):
            errors['loginEmail'] = 'No account with that email exists'

        elif not bcrypt.checkpw(postData['loginPassword'].encode(), user.password.encode()):
            errors['loginPassword'] = 'Incorrect Password'
        
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
