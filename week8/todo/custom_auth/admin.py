from django.contrib import admin
from .models import Profile

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'first_name', 'last_name', 'gender']


admin.site.register(Profile, ProfileAdmin)
