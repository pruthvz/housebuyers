from django.contrib import admin
from django.urls import path, include
from . import views
# All the urls linked with the accounts folder.
# so now you can access 'accounts/register' this is because we defined the 'accounts' in the main url.py file, the file which contained the settings.py
# now that we have 'accounts' we can access it and append more links to 'accounts/ like register'
urlpatterns = [
    path('register', views.register, name="register"),  # register.html
    path('login', views.login, name="login"),  # login.html
    path('logout', views.logout, name="logout"),  # logout request

]
