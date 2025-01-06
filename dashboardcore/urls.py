from django.urls import path, include, re_path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='home'),
    path('source/', include('sourcedata.urls', namespace='source')),
]
