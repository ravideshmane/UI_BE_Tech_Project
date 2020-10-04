from django.shortcuts import render

from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Designation, TechStack, EmploymentType, User
from .serializers import DesignationSerializer, TechStackSerializer, EmploymentTypeSerializer, UserSerializer

# Create your views here.

class DesignationApiView(ListCreateAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class DesignationApiModifyView(RetrieveUpdateDestroyAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class TechStackApiView(ListCreateAPIView):
    queryset = TechStack.objects.all()
    serializer_class = TechStackSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class TechStackApiModifyView(RetrieveUpdateDestroyAPIView):
    queryset = TechStack.objects.all()
    serializer_class = TechStackSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class EmploymentTypeApiView(ListCreateAPIView):
    queryset = EmploymentType.objects.all()
    serializer_class = EmploymentTypeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class EmploymentTypeApiModifyView(RetrieveUpdateDestroyAPIView):
    queryset = EmploymentType.objects.all()
    serializer_class = EmploymentTypeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class UserApiView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class UserModifyView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
