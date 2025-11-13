from django.db import models

class ContactMessage(models.Model):
    PROJECT_TYPES = [
        ("residential", "Residential"),
        ("commercial", "Commercial"),
        ("industrial", "Industrial"),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    company = models.CharField(max_length=200, blank=True)
    project_type = models.CharField(max_length=50, choices=PROJECT_TYPES, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
