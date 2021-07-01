from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("api", views.EmployeeModelViewSet, basename="emp")


urlpatterns = [

    path('', include(router.urls)),
    path('auth/', include("rest_framework.urls")),
 
]
