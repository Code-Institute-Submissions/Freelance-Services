from django.db import models

# Create your models here.

class Service(models.Model):
    """
    Services model used to display a service
    """
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return(self.name)

