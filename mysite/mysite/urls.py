"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path,include
# from . import views
# from home.views import *

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("",student,name="student"),
#     path("getStudents/",getStudents,name="getStudents"),
#     path("delete-student/<id>",delete_student,name="delete_student"),
#     # path('',views.index,name="index"),
#     # path('analyze',views.analyze,name="analyze")
# ]

from django.contrib import admin
from django.urls import path, include
from home.api import urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(urls)),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),
]



