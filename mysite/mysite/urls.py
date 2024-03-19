# Import admin module from django.contrib. This module provides the default Django admin interface.
from django.contrib import admin

# Import the path and include functions from django.urls.
# The path function is used to define URL patterns, and the include function is used to include URL configurations from other apps.
from django.urls import path, include

# Import the post_list view function from the views module of the blog app.
# This is necessary if you want to reference a view directly in the project's URL configuration.
from blog.views import post_list

# Define the urlpatterns list, which contains all URL patterns for the project.
urlpatterns = [
    # Map the URL 'admin/' to the admin site's built-in URLs.
    # This line is required to enable the Django admin interface for your project.
    path('admin/', admin.site.urls),
    
    # Include the URL configurations from the 'blog.urls' module under the 'blog/' path.
    # This means any URL patterns defined in 'blog/urls.py' are accessible under the 'blog/' prefix.
    # It's a way to delegate the handling of 'blog/' URLs to the blog app, keeping URL configurations modular.
    path('blog/', include('blog.urls')),

    path('', post_list),

    # Map the root URL ('') to the post_list view of the blog app.
    # This means that a request to 'http://yourdomain.com/' will be handled by the post_list view.
    # The name='home' argument assigns a name to this URL pattern, allowing it to be referred to by name elsewhere in the project.
    

    # Note: This line is a duplicate of the second path and should be removed to avoid confusion.
    # Including 'blog.urls' again under the same 'blog/' prefix is redundant and can lead to unexpected behavior.
    #path('blog/', include('blog.urls')),
]
