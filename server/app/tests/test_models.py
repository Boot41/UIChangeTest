from django.test import TestCase
from .models import Employer, JobListing

class EmployerModelTests(TestCase):
    def test_string_representation(self):
        employer = Employer(name='Test Employer', email='test@test.com')
        self.assertEqual(str(employer), employer.name)

class JobListingModelTests(TestCase):
    def setUp(self):
        self.employer = Employer.objects.create(name='Test Employer', email='test@test.com')

    def test_string_representation(self):
        job_listing = JobListing(employer=self.employer, title='Test Job')
        self.assertEqual(str(job_listing), job_listing.title)
