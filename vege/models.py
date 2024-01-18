from django.db import models

# Create your models here.
class Receipe(models.Model):
    receipe_name = models.CharField(max_length =100)
    receipe_desc = models.TextField()
    receipe_img = models.ImageField(upload_to="receipe")
