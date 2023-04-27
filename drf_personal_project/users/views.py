from django.shortcuts import render
from users.models import User
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from users.serializers import CustomTokenObtainPairSerializer, UserSerializer, UserDetailSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        # if문 없이 raise_exception을 사용하면 알아서 상태메시지까지 전달
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message":"가입완료!"}, status=status.HTTP_201_CREATED)

class UserDetailView(APIView):
    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)




class CustomTokenObtainPairView(TokenObtainPairView):
    # 최신 버전의 docs에는 없는데 무슨 차이가 있는지 알아보기 
    serializer_class = CustomTokenObtainPairSerializer

class mockView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        print(request.user)
        return Response("get 요청")


# 로그인 POST
# 로그아웃 POST
# 회원정보 수정 PUT
# 회원 탈퇴 DELETE
