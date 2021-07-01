from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


# router = DefaultRouter()
# router.register("api", views.EmployeeModelViewSet, basename="emp")


urlpatterns = [

    # >>>>>>>>>>>>>>>>>> using different functions <<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # path('api/', views.EmployeeDetail, name="emp"),
    # path('api/create/', views.EmployeeCreate, name="create"),
    # path('api/update/', views.EmployeeUpdate, name="update"),
    # path('api/delete/', views.EmployeeDelete, name="delete"),



    # >>>>>>>>>>>>>>>>>> using a single function <<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # path('api/', views.EmployeeCRUD, name="emp"),



    # >>>>>>>>>>>>>>>>> using a CBV <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # path('api/', views.EmployeeCBV.as_view(), name="emp"),



    # >>>>>>>>>>>>>>>>>>>>> APIViews <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # path('api/', views.EmployeeAPIViewFunction, name="emp"),
    # path('api/', views.EmployeeAPIViewCBV.as_view(), name="emp"),




    # >>>>>>>>>>>>>>>>>>>>> Generic APIViews <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


    # >>>>>>>>>>>>>>>>>>>> using different CBVs <<<<<<<<<<<<<<<<<<<<<<<<<<<

    # path('api/<int:pk>/', views.EmployeeRetrieveModelMixin.as_view(), name="emp"),
    # path('api/', views.EmployeeListModelMixin.as_view(), name="emp"),
    # path('api/', views.EmployeeCreateModelMixin.as_view(), name="create"),
    # path('api/<int:pk>/', views.EmployeeUpdateModelMixin.as_view(), name="update"),
    # path('api/<int:pk>/', views.EmployeeDestroyModelMixin.as_view(), name="delete"),
    


    # >>>>>>>>>>>>>>>>>>>> using 2 CBVs <<<<<<<<<<<<<<<<<<<<<<<<<<<

    # path('api/', views.Employee_List_Create_ModelMixin.as_view(), name="all_create"),
    # path('api/<int:pk>/', views.Employee_Retrieve_Update_Destroy_ModelMixin.as_view(), name="get_update_delete"),
    



    # >>>>>>>>>>>>>>>>>> using concrete views <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # path('api/', views.EmployeeListCreateAPIView.as_view(), name="list_create"),
    # path('api/<int:pk>/', views.EmployeeRetrieveUpdateDestroyAPIView.as_view(), name="get_update_delete"),







    # >>>>>>>>>>>>>>>>>>>> using ViewSets <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # path('', include(router.urls)),




    # >>>>>>>>>>>>>>>>>>>> using ModelViewSets <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    path('', include("app.api.urls")),



    # >>>>>>>>>>>>>>>>>>>> using Session Authentication <<<<<<<<<<<<<<<<<<<<

    path('auth/', include("rest_framework.urls")),
    
    
    

    # >>>>>>>>>>>>>>>>>>>>> generating a DRF token <<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # path('gettoken/', obtain_auth_token),


    
    # >>>>>>>>>>>>>>>>>>> generating a JWT token <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # path('gettoken/', TokenObtainPairView.as_view(), name="get"),
    # path('refreshtoken/', TokenRefreshView.as_view(), name="refresh"),
    # path('verifytoken/', TokenVerifyView.as_view(), name="verify"),


]
