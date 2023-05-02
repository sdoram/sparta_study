from django.urls import path
from todo import views

urlpatterns = [
    path('', views.TodoView.as_view()),
    path('<pk>/', views.TodoView.as_view()),
    path('<pk>/complete/', views.TodoCompleteView.as_view()),
]
