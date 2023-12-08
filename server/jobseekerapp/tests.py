from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import JobSeeker, Employer, Job, JobApplication

class ModelTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword',
            email='testuser@example.com',
            user_type='jobseeker'
        )
        self.employer = Employer.objects.create(
            user=self.user,
            employer_name='Test Employer',
            email='employer@example.com'
        )
        self.job_seeker = JobSeeker.objects.create(
            user=self.user,
            name='Test Job Seeker',
            email='jobseeker@example.com',
            phone_number='123456789',
            resume='path/to/resume.pdf',
            skills='Python, Django, JavaScript'
        )
        self.job = Job.objects.create(
            title='Software Developer',
            company_name='Test Company',
            description='Job description goes here.',
            location='Test Location',
            skills_required='Python, Django',
            salary_range='50000-70000',
            employer=self.employer
        )
        self.job_application = JobApplication.objects.create(
            job_seeker=self.job_seeker,
            job=self.job
        )

    def test_user_model(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.get_full_name(), 'testuser')
        self.assertEqual(self.user.user_type, 'jobseeker')

    def test_employer_model(self):
        self.assertEqual(str(self.employer), 'Test Employer')
        self.assertEqual(self.employer.user, self.user)

    def test_job_seeker_model(self):
        self.assertEqual(str(self.job_seeker), 'Test Job Seeker')
        self.assertEqual(self.job_seeker.user, self.user)

    def test_job_model(self):
        self.assertEqual(str(self.job), 'Software Developer')
        self.assertEqual(self.job.employer, self.employer)

    def test_job_application_model(self):
        expected_str = f"{self.job_seeker.name} applied for {self.job.title} on {self.job_application.application_date} (Status: {JobApplication.PENDING})"
        self.assertEqual(str(self.job_application), expected_str)


class ViewTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword',
            email='testuser@example.com',
            user_type='jobseeker'
        )
        self.employer = Employer.objects.create(
            user=self.user,
            employer_name='Test Employer',
            email='employer@example.com'
        )
        self.job_seeker = JobSeeker.objects.create(
            user=self.user,
            name='Test Job Seeker',
            email='jobseeker@example.com',
            phone_number='123456789',
            resume='path/to/resume.pdf',
            skills='Python, Django, JavaScript'
        )
        self.job = Job.objects.create(
            title='Software Developer',
            company_name='Test Company',
            description='Job description goes here.',
            location='Test Location',
            skills_required='Python, Django',
            salary_range='50000-70000',
            employer=self.employer
        )

    def test_job_list_view(self):
        response = self.client.get(reverse('job-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Software Developer')

    def test_job_detail_view(self):
        response = self.client.get(reverse('job-detail', args=[self.job.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Software Developer')

    def test_job_application_view(self):
        response = self.client.post(reverse('my-applications'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Application submitted successfully.')

    def test_welcome_view(self):
        response = self.client.get(reverse('welcome_view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome to JobSeekerApp API!')

    def test_job_seeker_viewset(self):
        response = self.client.get(reverse('jobseeker-list'))
        self.assertEqual(response.status_code, 200)


    def test_employer_viewset(self):
        response = self.client.get(reverse('employer-list'))
        self.assertEqual(response.status_code, 200)


    def test_job_viewset(self):
        response = self.client.get(reverse('job-list'))
        self.assertEqual(response.status_code, 200)


    def test_job_application_viewset(self):
        response = self.client.get(reverse('jobapplication-list'))
        self.assertEqual(response.status_code, 200)
        
    # def test_register_user_view(self):
    #     response = self.client.get(reverse('register_user'))
    #     self.assertEqual(response.status_code, 200)
    
    # def test_register_user_form_submission(self):
    #     data = {
    #         'username': 'testuser',
    #         'password1': 'testpassword',
    #         'password2': 'testpassword',
    #     }
    #     response = self.client.post(reverse('login'), data, follow=True)
    #     self.assertEqual(response.status_code, 302)
