from django.db import models

# Create your models here.
class user_created_blog(models.Model):
    user=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=100)
    content=models.CharField(max_length=1000000000)

    class Meta:
        ordering=['-date']
    def __str__(self) -> str:
        return self.date