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


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>> using 2 urls <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# def EmployeeList(request):
#     emps = Employee.objects.all()
#     serialized_emps = EmployeeSerializer(instance=emps, many=True)
#     json_string = JSONRenderer().render(serialized_emps.data)
#     return HttpResponse(json_string, content_type = "application/json")
#     # return HttpResponse(json_string)


# def EmployeeList(request):
#     emps = Employee.objects.all()
#     serialized_emps = EmployeeSerializer(instance=emps, many=True)
#     return JsonResponse(serialized_emps.data, safe=False)


# def EmployeeDetail(request, id):
#     emp = Employee.objects.get(id=id)
#     serialized_emp = EmployeeSerializer(instance=emp)
#     json_string = JSONRenderer().render(serialized_emp.data)
#     return HttpResponse(json_string, content_type = "application/json") # to render a json string
#     # return HttpResponse(json_string)  # to render a normal string


# def EmployeeDetail(request, id):
#     emp = Employee.objects.get(id=id)
#     serialized_emp = EmployeeSerializer(instance=emp)
#     return JsonResponse(serialized_emp.data) 
    

# >>>>>>>>>>>>>>>>>>>>>>> using single url <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# >>>>>>>>>>>>>>>>>>>>>>>>> GET request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# def EmployeeDetail(request):
#     native_type = JSONParser().parse(io.BytesIO(request.body))
#     id = native_type.get("id", None)
#     if id is not None:
#         emp = Employee.objects.get(id=id)
#         native_type = EmployeeSerializer(instance=emp)
#         json_string = JSONRenderer().render(native_type.data)
#         return HttpResponse(json_string, content_type = "application/json")
#     emps = Employee.objects.all()
#     native_type = EmployeeSerializer(instance=emps, many=True)
#     json_string = JSONRenderer().render(native_type.data)
#     return HttpResponse(json_string, content_type = "application/json")
#     # return HttpResponse(json_string)


# >>>>>>>>>>>>>>>>>>>>>>>>> POST request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# @csrf_exempt
# def EmployeeCreate(request):    
#     if request.method == "POST":
#         native_type = JSONParser().parse(io.BytesIO(request.body))
#         complex_type = EmployeeSerializer(data=native_type)
#         if complex_type.is_valid():
#             complex_type.save()
#             status = {
#                 "result" : "Employee Created!"
#             }
#             json_string = JSONRenderer().render(status)
#             return HttpResponse(json_string, content_type="application/json")
#         if complex_type.errors:
#             json_string = JSONRenderer().render(complex_type.errors)
#             return HttpResponse(json_string, content_type="application/json")


# >>>>>>>>>>>>>>>>>>>>>>> PUT request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# @csrf_exempt
# def EmployeeUpdate(request):
#     if request.method == "PUT":
#         native_type = JSONParser().parse(io.BytesIO(request.body))
#         id = native_type.get("id", None)
#         if id is not None:
#             emp = Employee.objects.get(id=id)
#             complex_type = EmployeeSerializer(instance=emp, data=native_type, partial=True)
#             if complex_type.is_valid():
#                 complex_type.save()
#                 status = {
#                     "result" : "Employee Updated!"
#                 }
#                 json_string = JSONRenderer().render(status)
#                 return HttpResponse(json_string, content_type="application/json")
#             if complex_type.errors:
#                 json_string = JSONRenderer().render(complex_type.errors)
#                 return HttpResponse(json_string, content_type="application/json")
#         status = {
#                     "result" : "Please provide a valid ID!"
#             }
#         json_string = JSONRenderer().render(status)
#         return HttpResponse(json_string, content_type="application/json")


# >>>>>>>>>>>>>>>>>>>>>>> DELETE request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# @csrf_exempt
# def EmployeeDelete(request):
#     if request.method == "DELETE":
#         native_type = JSONParser().parse(io.BytesIO(request.body))
#         id = native_type.get("id", None)
#         if id is not None:
#             emp = Employee.objects.get(id=id)
#             emp.delete()
#             status = {
#                     "result" : "Record Deleted!"
#             }
#             json_string = JSONRenderer().render(status)
#             return HttpResponse(json_string, content_type="application/json")
#         status = {
#                 "result" : "Please provide a valid ID!"
#         }
#         json_string = JSONRenderer().render(status)
#         return HttpResponse(json_string, content_type="application/json")





# >>>>>>>>>>>>>>>>>>>> using single function <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# @csrf_exempt
# def EmployeeCRUD(request):

#     #>>>>>>>>>>>>>>>>>>>>> GET request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#     if request.method == "GET":
#         native_type = JSONParser().parse(io.BytesIO(request.body))
#         id = native_type.get("id", None)
#         if id is not None:
#             emp = Employee.objects.get(id=id)
#             native_type = EmployeeSerializer(instance=emp)
#             json_string = JSONRenderer().render(native_type.data)
#             return HttpResponse(json_string, content_type = "application/json")
#         emps = Employee.objects.all()
#         native_type = EmployeeSerializer(instance=emps, many=True)
#         json_string = JSONRenderer().render(native_type.data)
#         return HttpResponse(json_string, content_type = "application/json")
#         # return HttpResponse(json_string)


    #>>>>>>>>>>>>>>>>>>>>>> POST request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # elif request.method == "POST":
    #     native_type = JSONParser().parse(io.BytesIO(request.body))
    #     complex_type = EmployeeSerializer(data=native_type)
    #     if complex_type.is_valid():
    #         complex_type.save()
    #         status = {
    #             "result" : "Employee Created!"
    #         }
    #         json_string = JSONRenderer().render(status)
    #         return HttpResponse(json_string, content_type="application/json")
    #     if complex_type.errors:
    #         json_string = JSONRenderer().render(complex_type.errors)
    #         return HttpResponse(json_string, content_type="application/json")


    # >>>>>>>>>>>>>>>>>>>>>>> PUT request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # elif request.method == "PUT":
    #     native_type = JSONParser().parse(io.BytesIO(request.body))
    #     id = native_type.get("id", None)
    #     if id is not None:
    #         emp = Employee.objects.get(id=id)
    #         complex_type = EmployeeSerializer(instance=emp, data=native_type, partial=True)
    #         if complex_type.is_valid():
    #             complex_type.save()
    #             status = {
    #                 "result" : "Employee Updated!"
    #             }
    #             json_string = JSONRenderer().render(status)
    #             return HttpResponse(json_string, content_type="application/json")
    #         if complex_type.errors:
    #             json_string = JSONRenderer().render(complex_type.errors)
    #             return HttpResponse(json_string, content_type="application/json")
    #     status = {
    #                 "result" : "Please provide a valid ID!"
    #         }
    #     json_string = JSONRenderer().render(status)
    #     return HttpResponse(json_string, content_type="application/json")


    #>>>>>>>>>>>>>>>>>>>>>> DELETE request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # elif request.method == "DELETE":
    #     native_type = JSONParser().parse(io.BytesIO(request.body))
    #     id = native_type.get("id", None)
    #     if id is not None:
    #         emp = Employee.objects.get(id=id)
    #         emp.delete()
    #         status = {
    #                 "result" : "Record Deleted!"
    #         }
    #         json_string = JSONRenderer().render(status)
    #         return HttpResponse(json_string, content_type="application/json")
    #     status = {
    #             "result" : "Please provide a valid ID!"
    #     }
    #     json_string = JSONRenderer().render(status)
    #     return HttpResponse(json_string, content_type="application/json")








# >>>>>>>>>>>>>>>>>>>>>>>> Using a Class Based Normal View <<<<<<<<<<<<<<<<<<<

# @method_decorator(csrf_exempt, name="dispatch")
# class EmployeeCBV(View):

#     # >>>>>>>>>>>>>>>>>>>> GET request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#     def get(self, request, *args, **kwargs):
#         native_type = JSONParser().parse(io.BytesIO(request.body))
#         id = native_type.get("id", None)
#         if id is not None:
#             emp = Employee.objects.get(id=id)
#             native_type = EmployeeSerializer(instance=emp)
#             json_string = JSONRenderer().render(native_type.data)
#             return HttpResponse(json_string, content_type = "application/json")
#         emps = Employee.objects.all()
#         native_type = EmployeeSerializer(instance=emps, many=True)
#         json_string = JSONRenderer().render(native_type.data)
#         return HttpResponse(json_string, content_type = "application/json")
#         # return HttpResponse(json_string)

    
#     # >>>>>>>>>>>>>>>>>>>>>>>>>> POST request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#     def post(self, request, *args, **kwargs):
#         native_type = JSONParser().parse(io.BytesIO(request.body))
#         complex_type = EmployeeSerializer(data=native_type)
#         if complex_type.is_valid():
#             complex_type.save()
#             status = {
#                 "result" : "Employee Created!"
#             }
#             json_string = JSONRenderer().render(status)
#             return HttpResponse(json_string, content_type="application/json")
#         if complex_type.errors:
#             json_string = JSONRenderer().render(complex_type.errors)
#             return HttpResponse(json_string, content_type="application/json")


#     # >>>>>>>>>>>>>>>>>>> PUT request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#     def put(self, request, *args, **kwargs):
#         native_type = JSONParser().parse(io.BytesIO(request.body))
#         id = native_type.get("id", None)
#         if id is not None:
#             emp = Employee.objects.get(id=id)
#             complex_type = EmployeeSerializer(instance=emp, data=native_type, partial=True)
#             if complex_type.is_valid():
#                 complex_type.save()
#                 status = {
#                     "result" : "Employee Updated!"
#                 }
#                 json_string = JSONRenderer().render(status)
#                 return HttpResponse(json_string, content_type="application/json")
#             if complex_type.errors:
#                 json_string = JSONRenderer().render(complex_type.errors)
#                 return HttpResponse(json_string, content_type="application/json")
#         status = {
#                     "result" : "Please provide a valid ID!"
#             }
#         json_string = JSONRenderer().render(status)
#         return HttpResponse(json_string, content_type="application/json")


#     # >>>>>>>>>>>>>>>>>>>>>>>> DELETE request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#     def delete(self, request, *args, **kwargs):
#         native_type = JSONParser().parse(io.BytesIO(request.body))
#         id = native_type.get("id", None)
#         if id is not None:
#             emp = Employee.objects.get(id=id)
#             emp.delete()
#             status = {
#                     "result" : "Record Deleted!"
#             }
#             json_string = JSONRenderer().render(status)
#             return HttpResponse(json_string, content_type="application/json")
#         status = {
#                 "result" : "Please provide a valid ID!"
#         }
#         json_string = JSONRenderer().render(status)
#         return HttpResponse(json_string, content_type="application/json")






# >>>>>>>>>>>>>>>>>>>>>>>> using API views <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# @api_view(["GET", "POST", "PUT", "DELETE"])
# def EmployeeAPIViewFunction(request):


#     # >>>>>>>>>>>>>>>>>>>>>> GET request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#     if request.method == "GET":
#         id = request.data.get("id", None)
#         if id is not None:
#             try:
#                 emp = Employee.objects.get(id=id)
#             except:
#                 emp = None
#             if emp is not None:
#                 native_type = EmployeeSerializer(instance=emp)
#                 return Response(native_type.data)
#             else:
#                 return Response({
#                     "status" : "Employee not found!"
#                 })
#         emps = Employee.objects.all()
#         native_types = EmployeeSerializer(instance=emps, many=True)
#         return Response(native_types.data)


#     # >>>>>>>>>>>>>>>>>>>>> POST request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#     elif request.method == "POST":
#         complex_type = EmployeeSerializer(data=request.data)
#         if complex_type.is_valid():
#             complex_type.save()
#             return Response({
#                 "msg" : "Record Created"
#             })
#         return Response(complex_type.errors)


#     # >>>>>>>>>>>>>>>>>>>>>>> PUT request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#     elif request.method == "PUT":
#         id = request.data.get("id", None)
#         if id is not None:
#             try:
#                 emp = Employee.objects.get(id=id)
#             except:
#                 emp = None
#             if emp is not None:
#                 complex_type = EmployeeSerializer(instance=emp, data=request.data, partial=True)
#                 if complex_type.is_valid():
#                     complex_type.save()
#                     return Response({
#                         "msg" : "Record Updated"
#                     })
#             return Response({
#                 "error" : "Employee not found!"
#             })
#         return Response({
#             "error" : "Please provide a valid ID!"
#         })


#    # >>>>>>>>>>>>>>>>>>>>>>> DELETE request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#     elif request.method == "DELETE":
#         id = request.data.get("id", None)
#         if id is not None:
#             try:
#                 emp = Employee.objects.get(id=id)
#             except:
#                 emp = None
#             if emp is not None:
#                 emp.delete()
#                 return Response({
#                         "msg" : "Record Deleted!"
#                     })               
#             return Response({
#                         "msg" : "Employee not found!"
#                     }) 
#         return Response({
#                         "msg" : "Please provide a valid ID!"
#                     })
    






# >>>>>>>>>>>>>>>>>>> Class Based Normal API Views <<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# class EmployeeAPIViewCBV(APIView):


#     # >>>>>>>>>>>>>>>>>>>>>>> GET request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#     def get(self, request, format=None):
#         id = request.data.get("id", None)
#         if id is not None:
#             try:
#                 emp = Employee.objects.get(id=id)
#             except:
#                 emp = None
#             if emp is not None:
#                 native_type = EmployeeSerializer(instance=emp)
#                 return Response(native_type.data)
#             else:
#                 return Response({
#                     "status" : "Employee not found!"
#                 }, status=status.HTTP_404_NOT_FOUND)
#         emps = Employee.objects.all()
#         native_types = EmployeeSerializer(instance=emps, many=True)
#         return Response(native_types.data)
        

#     # >>>>>>>>>>>>>>>>>>>>>>> POST request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#     def post(self, request, format=None):
#         complex_type = EmployeeSerializer(data=request.data)
#         if complex_type.is_valid():
#             complex_type.save()
#             return Response({
#                 "msg" : "Record Created"
#             })
#         return Response(complex_type.errors)


#     # >>>>>>>>>>>>>>>>>>>>>>> PUT request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#     def put(self, request, format=None):
#         id = request.data.get("id", None)
#         if id is not None:
#             try:
#                 emp = Employee.objects.get(id=id)
#             except:
#                 emp = None
#             if emp is not None:
#                 complex_type = EmployeeSerializer(instance=emp, data=request.data, partial=True)
#                 if complex_type.is_valid():
#                     complex_type.save()
#                     return Response({
#                         "msg" : "Record Updated"
#                     })
#             return Response({
#                 "error" : "Employee not found!"
#             }, status=status.HTTP_404_NOT_FOUND)
#         return Response({
#             "error" : "Please provide a valid ID!"
#         }, status=status.HTTP_404_NOT_FOUND)


#     # >>>>>>>>>>>>>>>>>>>>>>> DELETE request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#     def delete(self, request, format=None):
#         id = request.data.get("id", None)
#         if id is not None:
#             try:
#                 emp = Employee.objects.get(id=id)
#             except:
#                 emp = None
#             if emp is not None:
#                 emp.delete()
#                 return Response({
#                         "msg" : "Record Deleted!"
#                     })               
#             return Response({
#                         "msg" : "Employee not found!"
#                     }, status=status.HTTP_404_NOT_FOUND) 
#         return Response({
#                         "msg" : "Please provide a valid ID!"
#                     }, status=status.HTTP_404_NOT_FOUND)
    








# >>>>>>>>>>>>>>>>>>>>>>>> Generic API Views <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# >>>>>>>>>>>>>>>>>> with different views <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 


    # >>>>>>>>>>>>>>>>>>>>>>> GET request (single record) <<<<<<<<<<<<<<<<<<<<

# class EmployeeRetrieveModelMixin(RetrieveModelMixin, GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)



#     # >>>>>>>>>>>>>>>>>>>>>>> GET request (all records) <<<<<<<<<<<<<<<<<<<<

# class EmployeeListModelMixin(ListModelMixin, GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)



#     # >>>>>>>>>>>>>>>>>>>>>>>> POST request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# class EmployeeCreateModelMixin(CreateModelMixin, GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)



#     # >>>>>>>>>>>>>>>>>>>>>>>> PUT request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# class EmployeeUpdateModelMixin(UpdateModelMixin, GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)



#     # >>>>>>>>>>>>>>>>>>>>>>>> DELETE request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# class EmployeeDestroyModelMixin(DestroyModelMixin, GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)









# >>>>>>>>>>>>>>>>>>>>>>>> Generic API Views <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# >>>>>>>>>>>>>>>>>> with combined views <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



    # >>>>>>>>>>>>>>>>> GET all and POST request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# class Employee_List_Create_ModelMixin(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)



#     # >>>>>>>>>>>>>>>>> GET one, PUT, DELETE request <<<<<<<<<<<<<<<<<<<<<<<<<<<

# class Employee_Retrieve_Update_Destroy_ModelMixin(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer


#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)





# >>>>>>>>>>>>>>>>>>>>>>>>> concrete views <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


    # >>>>>>>>>>>>>>>>>>>>>>>> GET single record <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# class EmployeeListAPIView(RetrieveAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer



#     # >>>>>>>>>>>>>>>>>>>>>>>> GET all records <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# class EmployeeListAPIView(ListAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer



#     # >>>>>>>>>>>>>>>>>>>>>>>> POST request <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# class EmployeeCreateAPIView(CreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer



#     # >>>>>>>>>>>>>>>>>>>>>>>> PUT request <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# class EmployeeUpdateAPIView(UpdateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer



#     # >>>>>>>>>>>>>>>>>>>>>>>> DELETE request <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# class EmployeeDestroyAPIView(DestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer



#     # >>>>>>>>>>>>>>>>>>>>>>>> GET all and POST requests <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# class EmployeeListCreateAPIView(ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer



#     # >>>>>>>>>>>>>>>>>>>>>>>> GET single, PUT, DELETE requests <<<<<<<<<<<<<<

# class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer








# >>>>>>>>>>>>>>>>>>>>>>>>>>>> ViewSets <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# class EmployeeViewSet(viewsets.ViewSet):


#     # >>>>>>>>>>>>>>>>>>>>>>> GET all records <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#     def list(self, request):
#         emps = Employee.objects.all()
#         native_types = EmployeeSerializer(instance=emps, many=True)
#         return Response(native_types.data)


#     # >>>>>>>>>>>>>>>>>>>>>>> GET single record <<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#     def retrieve(self, request, pk=None):
#         id = pk
#         if id is not None:
#             try:
#                 emp = Employee.objects.get(id=id)
#             except:
#                 emp = None
#             if emp is not None:
#                 native_type = EmployeeSerializer(instance=emp)
#                 return Response(native_type.data)
#             else:
#                 return Response({
#                     "status" : "Employee not found!"
#                 }, status=status.HTTP_404_NOT_FOUND)
#         emps = Employee.objects.all()
#         native_types = EmployeeSerializer(instance=emps, many=True)
#         return Response(native_types.data)
        

#     # >>>>>>>>>>>>>>>>>>>>>>> POST request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#     def create(self, request):
#         complex_type = EmployeeSerializer(data=request.data)
#         if complex_type.is_valid():
#             complex_type.save()
#             return Response({
#                 "msg" : "Record Created"
#             })
#         return Response(complex_type.errors)


#     # >>>>>>>>>>>>>>>>>>>>>>> PUT request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#     def update(self, request, pk):
#         id = pk
#         if id is not None:
#             try:
#                 emp = Employee.objects.get(id=id)
#             except:
#                 emp = None
#             if emp is not None:
#                 complex_type = EmployeeSerializer(instance=emp, data=request.data)
#                 if complex_type.is_valid():
#                     complex_type.save()
#                     return Response({
#                         "msg" : "Record Updated"
#                     })
#             return Response({
#                 "error" : "Employee not found!"
#             }, status=status.HTTP_404_NOT_FOUND)
#         return Response({
#             "error" : "Please provide a valid ID!"
#         }, status=status.HTTP_404_NOT_FOUND)



#     # >>>>>>>>>>>>>>>>>>>>>>> Partial Update request <<<<<<<<<<<<<<<<<<<<<<<<<<

#     def partial_update(self, request, pk):
#         id = pk
#         if id is not None:
#             try:
#                 emp = Employee.objects.get(id=id)
#             except:
#                 emp = None
#             if emp is not None:
#                 complex_type = EmployeeSerializer(instance=emp, data=request.data, partial=True)
#                 if complex_type.is_valid():
#                     complex_type.save()
#                     return Response({
#                         "msg" : "Record Updated"
#                     })
#             return Response({
#                 "error" : "Employee not found!"
#             }, status=status.HTTP_404_NOT_FOUND)
#         return Response({
#             "error" : "Please provide a valid ID!"
#         }, status=status.HTTP_404_NOT_FOUND)



#     # >>>>>>>>>>>>>>>>>>>>>>> DELETE request <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#     def destroy(self, request, pk):
#         id = pk
#         if id is not None:
#             try:
#                 emp = Employee.objects.get(id=id)
#             except:
#                 emp = None
#             if emp is not None:
#                 emp.delete()
#                 return Response({
#                         "msg" : "Record Deleted!"
#                     })               
#             return Response({
#                         "msg" : "Employee not found!"
#                     }, status=status.HTTP_404_NOT_FOUND) 
#         return Response({
#                         "msg" : "Please provide a valid ID!"
#                     }, status=status.HTTP_404_NOT_FOUND)
    





# >>>>>>>>>>>>>>>>>>>>>>>>>> ModelViewSet <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


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


