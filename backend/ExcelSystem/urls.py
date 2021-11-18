from django.contrib import admin
from django.urls import path,include
import Excel_api.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Excel_api.urls')),
]
