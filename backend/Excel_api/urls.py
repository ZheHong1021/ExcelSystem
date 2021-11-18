from django.urls import path,include
from Excel_api.views import ControlExcel

urlpatterns = [
    path('test/', ControlExcel.as_view()),
]
