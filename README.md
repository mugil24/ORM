# Ex02 Django ORM Web Application
## Date: 6-03-2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram
![alt text](<doc .png>)E

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py
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

admin.py
from django.contrib import admin
from.models import Book_details,Book_detailsAdmin
admin.site.register(Book_details,Book_detailsAdmin)
```
## OUTPUT

![output](<Screenshot 2024-02-28 093713.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
