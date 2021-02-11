"""housebuyers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from houses import views

# This is the main URL python where, where the url links are created. for example, the 'accounts/' would have something like 'accounts/register'
# and that can be declared within the accounts folder and inside the accounts url.py
urlpatterns = [
    # HOUSES RELATED URL LINKS IS LISTED HERE
    path('', include('houses.urls')),
    path('admin/', admin.site.urls),  # ADMIN URL LINK
    # ACCOUNTS URL LINKS LISTED HERE
    path('accounts/', include('accounts.urls')),
    # HOUSE LIST URL LINKS LISTED HERE
    path('list/', include('houselist.urls'))
]
