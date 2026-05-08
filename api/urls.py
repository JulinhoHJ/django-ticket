from django.urls import path
from services.views import (
    AreasView,
    ManageAreasView,
    SedesView,
    ManageSedesView,
    AreasSedesView,
    ManageAreasSedesView,
    CategoriesView,
    ManageCategoriesView
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

urlpatterns = [
    path('areas/', AreasView.as_view()),
    path('areas/<int:pk>/', ManageAreasView.as_view()),
    path('sedes/', SedesView.as_view()),
    path('sedes/<int:pk>/', ManageSedesView.as_view()),
    path('areas-sedes/', AreasSedesView.as_view()),
    path('areas-sedes/<int:pk>/', ManageAreasSedesView.as_view()),
    path('categories/', CategoriesView.as_view()),
    path('categories/<int:pk>/', ManageCategoriesView.as_view()),
]