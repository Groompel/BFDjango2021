from django.db import models
from django.contrib.auth.models import User

# Create your models here.

genders = [
    (0, 'Male'),
    (1, 'Female')
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(
        max_length=100, blank=False, null=False, default='First name')
    last_name = models.CharField(
        max_length=100, blank=False, null=False, default='Last name')
    gender = models.IntegerField(choices=genders)
    favorite_color = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
