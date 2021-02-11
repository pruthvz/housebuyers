from django.contrib import admin
from .models import House
# Register your models here.
admin.site.register(House)

# This one line of code will display the House data fields within the django admin dashboard which can only be seen by admins
