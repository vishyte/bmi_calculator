from django.contrib import admin
from django.urls import path
from BMI import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='Home'),
    path('result',views.bmi, name="result"),

]
