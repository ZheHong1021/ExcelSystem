from django.urls import path,include, re_path
from Excel_api.views import ControlExcel, DownloadReportView

urlpatterns = [
    path('excel_write/', ControlExcel.as_view()),
    # re_path(r'^excel_download$', DownloadReportView.as_view()),
    path('excel_download/', DownloadReportView.as_view()),
    path('folderList/', DownloadReportView.folderList),
]
