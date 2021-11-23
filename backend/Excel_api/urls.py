from django.urls import path,include
from Excel_api.views import ControlExcel

urlpatterns = [
    path('excel_write/', ControlExcel.as_view()),
    path('excel_read/', ControlExcel.as_view()),
]
