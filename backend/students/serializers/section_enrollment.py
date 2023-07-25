from rest_framework import serializers
from ..models import SectionEnrollment


class SectionEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionEnrollment
        fields = '__all__'
