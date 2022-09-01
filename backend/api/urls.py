from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.getData),
    path('create/', views.createData),
    path('update/', views.updateData),
    path('delete/', views.deleteData)
]
