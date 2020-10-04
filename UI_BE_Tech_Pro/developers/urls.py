from django.urls import path
from . import views
urlpatterns = [
    path('api/developers/<int:id>/', views.DevelopersApiModifyView.as_view()),
    path('api/developers/', views.DevelopersApiView.as_view()),
]
