from django.urls import path

from students import views

urlpatterns = [
    path('', views.StudentList.as_view(), name='list_endpoint'),
    path('<int:pk>/', views.StudentDetail.as_view(), name='records_endpoint'),
]
