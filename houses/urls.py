from django.contrib import admin
from django.urls import path
from . import views

# These are the links for the house that was declared in the settings page.
urlpatterns = [
    path("", views.index, name="index"),  # HOME PAGE
    path('create', views.insert_view),  # ADDING A HOUSE PAGE LINK
    path('delete/<int:id>', views.delete_view),  # DELETE A HOUSE LINK
    path('about', views.about, name="about"),  # A SIMPLE ABOUT PAGE LINK
    # A SIMPLE CONTACT US PAGE LINK
    path('contact', views.contact, name="contact"),
    path('list/<int:id>', views.displayView, name="displayView"),


]
