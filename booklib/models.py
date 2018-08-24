from django.db import models

# Create your models here.
class book(models.Model):
    book_name=models.CharField(max_length=48,primary_key=True)
    book_author=models.CharField(max_length=24)
    book_intro=models.CharField(max_length=512)
    book_uploadtime=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_name



