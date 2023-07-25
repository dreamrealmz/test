from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, SectionViewSet, SectionEnrollmentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'sections', SectionViewSet)
router.register(r'section-enrollments', SectionEnrollmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
