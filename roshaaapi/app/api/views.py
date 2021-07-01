from django.shortcuts import render
from rest_framework import serializers
from ..models import Employee
from ..throttling import BasicUserRateThrottle
from .serializers import EmployeeSerializer
from ..paginations import CustomPageNumberPagination
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle
from rest_framework.filters import SearchFilter, OrderingFilter



class EmployeeModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle, BasicUserRateThrottle]

    ordering_fields = ["salary"]
    filter_backends = [OrderingFilter]

    pagination_class = CustomPageNumberPagination

