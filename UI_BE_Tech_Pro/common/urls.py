from django.urls import path, include
from . import views
urlpatterns = [
    path('api/designation/<int:pk>/', views.DesignationApiModifyView.as_view()),
    path('api/designation/', views.DesignationApiView.as_view()),
    path('api/techStack/', views.TechStackApiView.as_view()),
    path('api/techStack/<int:pk>/', views.TechStackApiModifyView.as_view()),
    path('api/employmentType/<int:pk>/', views.EmploymentTypeApiModifyView.as_view()),
    path('api/employmentType/', views.EmploymentTypeApiView.as_view()),
    path('api/user/', views.UserApiView.as_view()),
    path('api/user/<int:pk>/', views.UserModifyView.as_view()),
]
