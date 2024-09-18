"""Defines URL's for blogs"""
from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
	path('', views.index, name = 'index'),
	#Page that shows all blog posts
	path('blogposts/', views.blogposts, name = 'blogposts'),
	#Page for adding a new topic
	path('new_blogpost/', views.new_blogpost, name = 'new_blogpost'),
	#Page for editing an entry
	path('edit_blogpost/<int:blogpost_id>/', views.edit_blogpost, name= 'edit_blogpost'),
]