from django.contrib import admin
from django.urls import path, include
from home.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('api_auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/', include('home.urls'))
]
