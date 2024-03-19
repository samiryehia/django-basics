# Import the models module from django.db to define our model fields and behavior.
from django.db import models
# Import the User model from django.contrib.auth.models. This model represents the authenticated users in Django.
from django.contrib.auth.models import User
# Import timezone from django.utils to handle timezone-aware datetime objects.
from django.utils import timezone

# Define a new model named Post, which inherits from models.Model.
# This inheritance makes Post a Django model, so it's saved in the database.
#Each model we define maps into a table in our database
#The fields here represent the columns, which are the structure of the data that will be stored in the databse.
#Data stored in the database are basically rows following the column fileds (structure) we have defined here.
class Post(models.Model):
    # Define a character field for the post title with a maximum length of 200 characters.
    # This field is required and must be provided when creating a Post instance.
    title = models.CharField(max_length=200)
    
    # Define a text field for the post's main text content.
    # TextField is suitable for long text without a maximum length.
    text = models.TextField()
    
    # Define a ForeignKey relationship to the User model.
    # This indicates that each Post is written by a User, establishing a many-to-one relationship.
    # on_delete=models.CASCADE argument ensures that if the referenced User is deleted,
    # all their Posts are also deleted, maintaining referential integrity.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Define a DateTimeField for the post creation date and time.
    # The default value is set to the current date and time using timezone.now().
    # This ensures that when a Post instance is created, its created_date is automatically set.
    created_date = models.DateTimeField(default=timezone.now)
    
    # Define an optional DateTimeField for the post publication date and time.
    # It's optional because blank=True (allowed to be blank in forms) and null=True (allowed to store NULL in the database).
    published_date = models.DateTimeField(blank=True, null=True)

    # Define a method named publish to "publish" the post.
    # When called, it sets the published_date of the instance to the current date and time,
    # and then saves the instance to the database.
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # Define the __str__ method to return a string representation of the Post instance.
    # This is particularly useful in the Django admin site or shell, where you can quickly identify objects by their title.
    def __str__(self):
        return self.title
