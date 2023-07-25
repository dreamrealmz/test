from rest_framework import viewsets
from ..models import SectionEnrollment
from ..serializers import SectionEnrollmentSerializer


class SectionEnrollmentViewSet(viewsets.ModelViewSet):
    queryset = SectionEnrollment.objects.all()
    serializer_class = SectionEnrollmentSerializer
