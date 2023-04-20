
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.registration),
    path('verify/', views.verifyuser),
    path('contactus/', views.contactus),
    path('ourwebsite', views.music)

]
