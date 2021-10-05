from functools import partial
from typing import SupportsAbs
from django.shortcuts import render
import requests
from rest_framework import serializers
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.mixins import (ListModelMixin, CreateModelMixin,
                                   RetrieveModelMixin, UpdateModelMixin,
                                   DestroyModelMixin)
from rest_framework.generics import (ListAPIView, CreateAPIView, UpdateAPIView,
                                     DestroyAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework import viewsets

from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import (IsAdminUser, IsAuthenticated, AllowAny,
                                        IsAuthenticatedOrReadOnly, DjangoModelPermissions,
                                        DjangoModelPermissionsOrAnonReadOnly)
from .custom_permissions import CustomPermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle
from .throttling import BasicUserRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import CustomPageNumberPagination



class EmployeeModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle, BasicUserRateThrottle]

    # filter_fields = ["name", "salary"]
    # filter_backends = [DjangoFilterBackend]

    # search_fields = ["name", "salary"]
    # filter_backends = [SearchFilter]

    ordering_fields = ["salary"]
    filter_backends = [OrderingFilter]

    pagination_class = CustomPageNumberPagination


    # >>>>>>>>>>>>>>>>>>> ReadOnly ModelViewSet <<<<<<<<<<<<<<<<<<<<<<<<<<

# class EmployeeModelViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer


