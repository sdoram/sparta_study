from django.urls import path
from user import views

urlpatterns = [
    path('', views.UserView.as_view()),
    path('login/', views.UserLoginView.as_view()),
    path('logout/', views.UserLogoutView.as_view()),
]