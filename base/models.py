from django.db import models

# Create your models here.
class testimonial(models.Model):
    name = models.CharField(max_length=200, null=True)
    message = models.CharField(max_length=300, null=True)
    pic = models.ImageField(upload_to='pics', null=True)

    def __str__(self):
        return self.name