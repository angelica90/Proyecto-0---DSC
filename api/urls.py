"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from api.core.api import UserAPI
from rest_framework.authtoken import views
from api.core.views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/create-user/', UserAPI.as_view() , name = 'api_create_user'),
    path('api/events/', event_list.as_view(), name = 'event_list'),
    path('api/api-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/events/<int:evento_id>/', event_detail.as_view(), name = 'detail_event_list'),
]