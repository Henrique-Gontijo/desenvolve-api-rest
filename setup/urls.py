"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from rest_framework import routers
from myflix.views import UserViewSet, StreamViewSet, ListViewSet, ListUser, ListStream

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('streams', StreamViewSet, basename='streams')
router.register('lists', ListViewSet, basename='lists')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('users/<int:pk>/lists/', ListUser.as_view()),
    path('streams/<int:pk>/lists/', ListStream.as_view()),
]
