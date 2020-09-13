from django.urls import path

from userapp import views

urlpatterns = [
    path('user/', views.UserAPIView.as_view()),
]