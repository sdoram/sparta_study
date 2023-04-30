from users.models import User
from .models import ToDoList
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from users.serializers import CustomTokenObtainPairSerializer, UserSerializer, UserDetailSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

class ToDoListView(APIView):
    def post(self, request):
        # to do list 생성 
        pass


class ToDoListDetailView(APIView):
    def get(self, request):
        # to do list 확인
        pass

    def put(self, request):
        # to do list 수정 
        pass

    def delete(self, request):
        # to do list DELETE
        pass