from django.db import models

# Create your models here.

class Service(models.Model):
    """
    Services model used to display a service
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    #images = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return(self.name)

