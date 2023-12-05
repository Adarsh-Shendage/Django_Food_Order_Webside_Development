"""registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.LoginPage,name='login'),
    path('SignupPage/',views.SignupPage,name='signup'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('about/',views.aboutpage,name='about'),
    path('veg/',views.veg_thali,name='veg_thali'),
    path('nonveg/',views.Nonveg_thali,name='Non_veg_thali'),
    path('chat/',views.chat,name='chat'),
    path('fastfood/',views.fastfood,name='fastfood'),
    path('soop/',views.soop,name='soop'),
    path('pasta/',views.pasta,name='pasta'),
    path('order/',views.order,name='order'),
    path('contact/',views.contact,name='contact'),






]
