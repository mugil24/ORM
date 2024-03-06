from django.db import models
from django.contrib import admin
class Book_details(models.Model):
      book_name=models.CharField(max_length=30);
      author_name=models.CharField(max_length=20);
      book_no=models.IntegerField(primary_key=True);
      book_price=models.IntegerField();
      published_year=models.IntegerField();
class Book_detailsAdmin(admin.ModelAdmin): 
      list_display=("book_name","book_no","author_name","book_price","published_year");
# Create your models here.
