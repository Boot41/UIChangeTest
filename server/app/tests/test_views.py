from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Employer, JobListing

class JobListingTests(APITestCase):
    def setUp(self):
        self.employer = Employer.objects.create(name='Test Employer', email='employer@test.com')

    def test_create_job_listing(self):
        url = reverse('job-listing-list')
        data = {
            'employer': self.employer.id,
            'title': 'Test Job',
            'description': 'Job description here',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_job_listings(self):
        JobListing.objects.create(employer=self.employer, title='Test Job 1', description='Description 1')
        JobListing.objects.create(employer=self.employer, title='Test Job 2', description='Description 2')
        url = reverse('job-listing-list', kwargs={'employer_id': self.employer.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_update_job_listing(self):
        job = JobListing.objects.create(employer=self.employer, title='Test Job', description='Job description')
        url = reverse('job-listing-detail', kwargs={'employer_id': self.employer.id, 'pk': job.id})
        data = {'title': 'Updated Job'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        job.refresh_from_db()
        self.assertEqual(job.title, 'Updated Job')

    def test_delete_job_listing(self):
        job = JobListing.objects.create(employer=self.employer, title='Test Job', description='Job description')
        url = reverse('job-listing-detail', kwargs={'employer_id': self.employer.id, 'pk': job.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(JobListing.objects.count(), 0)
