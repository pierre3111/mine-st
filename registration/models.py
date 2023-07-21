from django.db import models
from conferences.models import Conference

class Registration(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    job_role_choices = [
        ('Full Stack', 'Full Stack'),
        ('Backend', 'Backend'),
        ('Frontend', 'Frontend'),
        ('Designer', 'Designer'),
        ('Student', 'Student'),
    ]
    job_role = models.CharField(max_length=20, choices=job_role_choices)
    topics_interest_choices = [
        ('JavaScript Frameworks', 'JavaScript Frameworks'),
        ('JavaScript Libraries', 'JavaScript Libraries'),
        ('Node.js', 'Node.js'),
        ('Build Tools', 'Build Tools'),
    ]
    topics_interest = models.CharField(max_length=100, choices=topics_interest_choices)
    payment_card_number = models.CharField(max_length=16)
    zip_code = models.CharField(max_length=10)
    cvv = models.CharField(max_length=4)
    expiration_date = models.CharField(max_length=5)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name='registrations')

    def __str__(self):
        return f"{self.name} - {self.conference.name}"
