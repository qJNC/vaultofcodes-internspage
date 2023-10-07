from django.urls import path
from . import views

app_name = "codes"

urlpatterns = [
    path('', views.internship, name='internship_page'),
]