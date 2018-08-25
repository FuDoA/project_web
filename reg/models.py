from django.db import models

class user  (models.Model):
    id=models.CharField(max_length=24 , primary_key=True)
    salt=models.CharField(max_length=6)
    pswmd5=models.CharField(max_length=32)


