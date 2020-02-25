from django.db import models

# Create your models here.
class Todo(models.Model):
  added_date=models.DateTimeField()
  text=models.CharField(max_length=200)
  status=models.CharField(max_length=20,default='danger')

  def __str__(self):
      return self.text
  