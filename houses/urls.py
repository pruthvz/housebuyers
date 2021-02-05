from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path('create', views.insert_view),
    path('delete/<int:id>', views.delete_view),
    path('about', views.about, name="about")
]
