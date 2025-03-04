from django.db import models

class Complaint(models.Model):
    complaint_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)  # Allow NULL
    crime_location = models.TextField(null=True, blank=True)  # Allow NULL
    email = models.EmailField()
    phone = models.CharField(max_length=15, null=True, blank=True)  # Allow NULL
    crime_type = models.CharField(max_length=50)
    description = models.TextField()
    evidence_url = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, default="Pending")  # Status field is fine

    def __str__(self):
        return f"{self.complaint_id} - {self.name}"



class Admin(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username