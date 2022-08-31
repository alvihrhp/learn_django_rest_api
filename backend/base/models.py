from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    is_done = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
