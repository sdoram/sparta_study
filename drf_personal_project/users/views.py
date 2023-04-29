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
        # 검색 id로 User정보 검색 
        user = get_object_or_404(User, id=id)
        # 현재 user와 검색 user 일치 판단
        if request.user == user:
            serializer = UserDetailSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message":"본인이 아닙니다"}, status=status.HTTP_401_UNAUTHORIZED)
        
    def put(self, request, id):
        # 회원정보 수정 PUT
        user = get_object_or_404(User, id=id)
        serializer = UserDetailSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
        # if request.user == user:
        # else:
            # return Response({"message":"본인이 아닙니다"}, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, id):
        # 회원 탈퇴 DELETE
        pass




class CustomTokenObtainPairView(TokenObtainPairView):
    # 최신 버전의 docs에는 없는데 무슨 차이가 있는지 알아보기 
    serializer_class = CustomTokenObtainPairSerializer

class mockView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        print(request.user)
        return Response("get 요청")


# 로그인 POST <- users/api/token에서 로그인
# 로그아웃 POST <- token으로 로그인 유효 시간이 있는데 로그아웃 따로 되나? <- token 방식은 백엔드에서 일단 구현 안하고 넘어감


