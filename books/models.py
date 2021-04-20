from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class addBook(models.Model):
    bookid = models.IntegerField(primary_key = True)
    cost = models.IntegerField()
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class order(models.Model):
    studentname = models.CharField(max_length=100)
    bookname = models.CharField(max_length=100)
    issue_date = models.DateTimeField(auto_now_add=True, null=True)
    return_date = models.DateTimeField(default=datetime.now()+timedelta(days=15), null=True)

    def __str__(self):
        return self.studentname

        