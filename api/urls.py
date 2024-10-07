from django.contrib import admin
from django.urls import path, include
from api.views import CompanyViewSet,EmployeeViewSet
from rest_framework import routers


companyUrl = routers.DefaultRouter()
companyUrl.register(r'companies', CompanyViewSet)
employeeUrl = routers.DefaultRouter()
employeeUrl.register(r'employee', EmployeeViewSet)

urlpatterns = [
    path('', include(companyUrl.urls)),
    path('', include(employeeUrl.urls)),
]