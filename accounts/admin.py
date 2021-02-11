from django.contrib import admin
from .models import UserProfile
# Displays the Users details in the admin panel
admin.site.register(UserProfile)
