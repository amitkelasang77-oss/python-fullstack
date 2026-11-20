"""
URL configuration for college_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from student import views

urlpatterns = [

    # Admin
    path('admin/', admin.site.urls),

    # Home page
    path('home/', views.home, name='home'),

    # About and Contact
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # Student registration form
    path('student/', views.student_form, name='student_form'),

    # Login and Logout
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # User registration
    path('register/', views.register, name='register'),

    # Student Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    path('api/',views.student_api,name='student_api')

]
