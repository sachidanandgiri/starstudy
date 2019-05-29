"""starstdy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'study'
urlpatterns = [
    path('', views.index, name='index'),
    path('feature', views.feature, name='feature'),
    path('price', views.price, name='price'),
    path('blog', views.blog, name='blog'),
    path('blog_details', views.blog_details, name='blog_details'),
    path('contact', views.contact, name='contact'),
    path('register', views.register, name='register'),
    path('student', views.student, name='student'),
    path('login', views.login, name='login'),
    path('user_logout', views.user_logout, name='user_logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
