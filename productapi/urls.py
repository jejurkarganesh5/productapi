
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

swagger_view = get_swagger_view(title='BRAND-PRODUCT API')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'swagger/', swagger_view),
    path('api/', include('productapp.urls'))
]
