"""
URL configuration for car_selling_project project.

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
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name = 'homepage'),
    path('brand/<slug:slug>/', views.home, name ='brand_wise_car'),
    path('signup/', views.SignUpView.as_view(), name ='signup'),
    path('login/', views.LoginView.as_view(), name ='login'),
    path('logout/',views.user_logout,name = 'logout'),            
    path('profile/',views.profile,name = 'profile'),  
    path('edit_profile/',views.EditUserView.as_view(),name = 'edit_profile'),  
    path('car/',include('car.urls'))          
]
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
