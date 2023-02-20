from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import StudentSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.

class StudentView(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


# class StudentView(viewsets.ViewSet):
    # def list(self, request):
    #     queryset = Student.objects.all()
    #     serializer = StudentSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = Student.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = StudentSerializer(user)
    #     return Response(serializer.data)