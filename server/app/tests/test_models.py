from django.test import TestCase
from .models import Employer, JobListing

class JobListingModelTests(TestCase):

    def setUp(self):
        self.employer = Employer.objects.create(name='Test Employer', email='employer@test.com')

    def test_job_listing_creation(self):
        job = JobListing.objects.create(employer=self.employer, title='Job 1', description='Description 1')
        self.assertEqual(job.title, 'Job 1')
        self.assertEqual(job.employer, self.employer)
        self.assertTrue(job.is_active)

    def test_job_str_method(self):
        job = JobListing.objects.create(employer=self.employer, title='Job 1', description='Description 1')
        self.assertEqual(str(job), 'Job 1')
