from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from users.serializers import UserSerializer


class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        # if문 없이 raise_exception을 사용하면 알아서 상태메시지까지 전달
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message":"가입완료!"}, status=status.HTTP_201_CREATED)


# 회원가입 POST
# 로그인 POST
# 로그아웃 POST
# 회원정보 수정 PUT
# 회원 탈퇴 DELETE
