from django.urls import path,include
from Excel_api.views import ControlExcel,GetExcel

urlpatterns = [
    path('excel_write/', ControlExcel.as_view()),
    path('excel_read/', GetExcel.as_view()),
]
