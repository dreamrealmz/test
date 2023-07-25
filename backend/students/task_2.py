from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Student
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated


#
# class StudentSerializer(serializers.ModelSerializer):
#     school_number = serializers.IntegerField(source='school.number')
#
#     class Meta:
#         model = Student
#         fields = ['id', 'name', 'age', 'specialization', 'school_number']
#
#
# class StudentsAPIView(APIView):
#     def get(self, request):
#         if request.user and request.user.is_authenticated:
#             queryset = Student.objects.all()
#             serializer = StudentSerializer(queryset)
#             return Response(serializer.data)
#         return Response(status=403)


# мое решение в заданном стиле
class StudentSerializer(serializers.ModelSerializer):
    school_number = serializers.PrimaryKeyRelatedField(source='school', read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'specialization', 'school_number']


class StudentsAPIView(ListAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes = [IsAuthenticated]
