from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import JobListing
from .serializers import JobListingSerializer

class JobListingViewSet(viewsets.ModelViewSet):
    queryset = JobListing.objects.all()
    serializer_class = JobListingSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, employer_id, *args, **kwargs):
        jobs = JobListing.objects.filter(employer_id=employer_id)
        serializer = self.get_serializer(jobs, many=True)
        return Response(serializer.data)
