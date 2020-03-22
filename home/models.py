from django.db import models

# Create your models here.


class HomePage(models.Model):
    """
    Used for freelancers to configure values in the admin panel, this allows them to customise there site.
    """
    title = "Home Page (You can only have 1 of these)"
    name = models.CharField(max_length=20, blank=False)
    headline = models.CharField(max_length=50, blank=False)
    subheadline = models.CharField(max_length=100, blank=False)
    about = models.TextField(blank=False)

    # Allows for only one home page to be created
    @classmethod
    def object(cls):
        return cls._default_manager.all().first()  

    def save(self, *args, **kwargs):
        self.id = 1
        return super().save(*args, **kwargs)

    def __str__(self):
        return(self.title)

