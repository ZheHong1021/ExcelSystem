from django.contrib import admin
from django.urls import path,include, re_path
import Excel_api.urls
from django.views.generic import TemplateView

urlpatterns = [
    re_path(r'^$', TemplateView.as_view(template_name="index.html")), # 新增的
    path('admin/', admin.site.urls),
    path('api/', include('Excel_api.urls')),
]
