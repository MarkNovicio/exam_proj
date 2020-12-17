import re
from django.db import models
from login_app.models import Registration

class QuoteManager(models.Manager):
    def basic_validator(self, post_data):
        errors ={}
        if len(post_data['quote_author']) < 2:
            errors['quote_author'] = "Quoted by should be 2 or more characters"
        if len(post_data['quote']) < 11:
            errors['quote'] = "Message should be 10 or more characters"
        return errors
    
    def edit_validator(self, post_data):
        errors = {}
        if len(post_data['quote_author']) < 2:
            errors['quote_author'] = "Quoted by should be 2 or more characters"
        if len(post_data['quote']) < 11:
            errors['quote'] = "Message should be 10 or more characters"
        return errors
   
class Quotes(models.Model):
    publisher = models.ForeignKey(Registration, related_name="quotes", on_delete =models.CASCADE)
    quote_author = models.CharField(max_length=1000)
    quote = models.CharField(max_length=1000)
    favorites = models.ManyToManyField(Registration, related_name = "favorite_quotes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = QuoteManager()

