from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPES = [
        ('employer', 'Employer'),
        ('jobseeker', 'Job Seeker'),
    ]

    user_type = models.CharField(max_length=20, choices=USER_TYPES)

class JobSeeker(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    resume = models.FileField(upload_to='resumes/')
    skills = models.CharField(max_length=600)

    def __str__(self):
        return self.name

class Employer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    employer_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.employer_name

class Job(models.Model):
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    skills_required = models.CharField(max_length=600)
    salary_range = models.CharField(max_length=50)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='jobs')

    def __str__(self):
        return self.title

class JobApplication(models.Model):
    PENDING = 'Pending'
    APPROVED = 'Approved'
    REJECTED = 'Rejected'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    ]

    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    

    def __str__(self):
        return f"{self.job_seeker.name} applied for {self.job.title} on {self.application_date} (Status: {self.status})"