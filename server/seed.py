import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")

import django
django.setup()

from django.contrib.auth import get_user_model
from jobseekerapp.models import Employer, Job, JobSeeker, JobApplication
from faker import Faker

fake = Faker()
User = get_user_model()


# Delete existing data
Employer.objects.all().delete()
JobSeeker.objects.all().delete()
Job.objects.all().delete()
JobApplication.objects.all().delete()


employers = []
job_seekers = []

for _ in range(10):
    employer = User.objects.create_user(
        username=fake.user_name(),
        email=fake.email(),
        password="password",
        user_type="employer",
    )
    Employer.objects.create(
        user=employer,
        employer_name=fake.company(),
        email=employer.email,
        phone_number=fake.phone_number(),
    )
    employers.append(employer)

for _ in range(10):
    job_seeker = User.objects.create_user(
        username=fake.user_name(),
        email=fake.email(),
        password="password",
        user_type="jobseeker",
    )
    JobSeeker.objects.create(
        user=job_seeker,
        name=fake.name(),
        email=job_seeker.email,
        phone_number=fake.phone_number(),
        resume=fake.file_name(category="resume", extension="pdf"),
        skills=" ".join(fake.words(5)),
    )
    job_seekers.append(job_seeker)

# Create jobs
job_titles = ["Software Engineer", "Software Developer", "Data Scientist", "DevOps Engineer", "Data Analyst", "Data Engineer", "Salesforce Engineer", "UI/UX Designer", "Cyber Security", "Quality Assurance", ]
locations = ["Nairobi", "Beijing", "New York", "London", "Paris"]
salary_ranges = ["50,000 - 80,000 Ksh", "70,000 - 100,000 Ksh", "90,000 - 120,000 Ksh"]
job_types = ["Full-time", "Part-time", "Remote", "Hybrid"]

for i in range(10):
    employer = Employer.objects.get(user=employers[i])
    title = job_titles[i]
    company_name = employer.employer_name
    description = fake.text()
    location = fake.random_element(locations)
    date_posted = fake.date_time_this_decade()
    job_type = fake.random_element(job_types)
    skills_required = " ".join(fake.words(5))
    salary_range = fake.random_element(salary_ranges)

    Job.objects.create(
        title=title,
        company_name=company_name,
        description=description,
        location=location,
        date_posted=date_posted,
        job_type=job_type,
        skills_required=skills_required,
        salary_range=salary_range,
        employer=employer,
    )

# Create job applications
for job_seeker in job_seekers:
    job = Job.objects.order_by("?").first()
    JobApplication.objects.create(
        job_seeker=JobSeeker.objects.get(user=job_seeker),
        job=job,
        status=fake.random_element(elements=[JobApplication.PENDING, JobApplication.APPROVED, JobApplication.REJECTED]),
    )

print("Database seeding complete.")
