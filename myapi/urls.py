# myapi/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('',views.apisupported, name='supported_api'),
    path('homework-list/', views.allhomework, name="homework-list"),
	path('homework-detail/<str:pk>/', views.homeworkdetail, name="homework-detail"),
	path('homework-create/', views.createhomework, name="homework-create"),

	path('homework-update/<str:pk>/', views.updatehomework, name="homework-update"),
	path('homework-delete/<str:pk>/', views.deletehomework, name="homework-delete"),
]