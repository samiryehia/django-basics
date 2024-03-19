# Import the path function from django.urls. 
# This function is used to define individual URL patterns.
from django.urls import path

# Import the views module from the current package (denoted by '.').
# This allows us to refer to views defined in the views.py file of the current Django app.
from . import views

# Define a list named urlpatterns. 
# This list is a Django convention for URL configuration and will contain all the URL patterns for this app.
urlpatterns = [
    # Define the first URL pattern:
    # An empty string as the first argument means this pattern matches the root URL for this app.
    # views.post_list is the view function that will be called if this URL pattern is matched.
    # The name='post_list' argument assigns a name to this URL pattern, allowing it to be referred to in templates and view functions.
    path('', views.post_list, name='post_list'),
    #'/blog' is the prefix that is defined in the PROJECT urls.py file
    #'allposts' is the path that we define AFTER the prefix set in the urls PROJECT FILE.
    #So this is the path that we get at the end localhost:8000/blog/allposts.
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),

]
