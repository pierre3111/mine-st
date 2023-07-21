from django.db import models

class Conference(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    date = models.DateField()
    venue = models.CharField(max_length=255)
    theme = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Speaker(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    contact_info = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='speakers/', blank=True, null=True)
    areas_of_expertise = models.TextField()

    def __str__(self):
        return self.name
