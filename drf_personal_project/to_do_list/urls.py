from django.urls import path
from to_do_list import views


urlpatterns = [
    path('create/', views.ToDoListView.as_view(), name='user_view'),
    path('<int:id>', views.ToDoListDetailView.as_view(), name='user_detail_view'),
]
