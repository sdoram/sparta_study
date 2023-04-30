from users.models import User
from rest_framework.views import APIView
from rest_framework import status
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
    
    
    def get(self, request):
        users = User.objects.all()
        serializer = UserDetailSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserDetailView(APIView):
    def get(self, request,id):
        user = get_object_or_404(User, id=id)
        if request.user == user:
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message":"본인이 아닙니다"}, status=status.HTTP_403_FORBIDDEN)

    def put(self, request, id):
        # 회원정보 수정 PUT
        user = get_object_or_404(User, id=id)
        serializer = UserDetailSerializer(user,data=request.data)
        # 현재 user와 검색 user 일치 판단
        if request.user == user:
            serializer.is_valid(raise_exception=True)
            password = request.data.get("password")
            user.set_password(password)
            serializer.save(password=user.password)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message":"본인이 아닙니다"}, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, id):
        # 회원 탈퇴 DELETE
        user = get_object_or_404(User, id=id)
        if request.user == user:
            user.delete()
            return Response({"message":"탈퇴 완료!"},status=status.HTTP_200_OK)
        else:
            return Response({"message":"본인이 아닙니다"}, status=status.HTTP_401_UNAUTHORIZED)


class CustomTokenObtainPairView(TokenObtainPairView):
    # 최신 버전의 docs에는 없는데 무슨 차이가 있는지 알아보기 
    serializer_class = CustomTokenObtainPairSerializer


