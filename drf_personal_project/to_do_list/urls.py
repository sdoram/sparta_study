from django.urls import path
from to_do_list import views


urlpatterns = [
    path('', views.ToDoListView.as_view(), name='to_do_list_view'),
    path('<int:id>/', views.ToDoListDetailView.as_view(), name='to_do_list_detail_view'),
]
