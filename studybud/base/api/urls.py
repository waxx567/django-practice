from django.urls import path
from . import views

urlpatterns = [
    path('routes/', views.getRoutes),
    path('rooms/', views.getRooms),
    path('rooms/<str:pk>', views.getRoom),
]