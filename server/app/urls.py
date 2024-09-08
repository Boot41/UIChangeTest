from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobListingViewSet

router = DefaultRouter()
router.register(r'jobs', JobListingViewSet, basename='job-listing')

urlpatterns = [
    path('employers/<int:employer_id>/', include(router.urls)),
]