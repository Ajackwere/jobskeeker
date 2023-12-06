from django.contrib import admin
from .models import JobSeeker, Employer, Job, JobApplication

@admin.register(JobSeeker)
class JobSeekerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')
    search_fields = ('name', 'email')

@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('employer_name', 'email')
    search_fields = ('employer_name', 'email')

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company_name', 'location', 'employer')
    search_fields = ('title', 'company_name', 'location')
    list_filter = ('employer',)

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('job_seeker', 'job', 'application_date')
    search_fields = ('job_seeker__name', 'job__title')
    list_filter = ('job', 'application_date')
