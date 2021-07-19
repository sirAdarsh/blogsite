from django.contrib import admin
from django.urls import path
from .views import *
 
urlpatterns = [
    path('', BlogListView, name='blogs'),
    path('blog/<int:_id>', BlogDetailView, name='blog'),
]