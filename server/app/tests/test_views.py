from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Employer, JobListing

class JobListingTests(APITestCase):

    def setUp(self):
        self.employer = Employer.objects.create(name='Test Employer', email='employer@test.com')

    def test_create_job_listing(self):
        url = reverse('job-listing-list', kwargs={'employer_id': self.employer.id})
        data = {'employer': self.employer.id, 'title': 'Test Job', 'description': 'Job Description'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_job_listings(self):
        JobListing.objects.create(employer=self.employer, title='Test Job 1', description='Job 1 Description')
        JobListing.objects.create(employer=self.employer, title='Test Job 2', description='Job 2 Description')
        url = reverse('job-listing-list', kwargs={'employer_id': self.employer.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_job_listing_invalid(self):
        url = reverse('job-listing-list', kwargs={'employer_id': self.employer.id})
        data = {'title': 'Invalid Job'}  # Missing 'employer' and 'description'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
