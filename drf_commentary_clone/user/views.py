from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from user.models import User
from user.serializers import UserSerializer


class UserView(APIView):
    def get(self, request):
        """ 사용자 정보를 response 합니다. """

        return Response(UserSerializer(request.user).data)
    
    def post(self, request):
        """ 사용자 정보로 회원 가입 합니다. """
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save() # UserSerializer.create()실행

        return Response({'message': 'post 요청입니다!'})
    
    def put(self, request):
        """ 회원 정보를 수정 합니다. """

        return Response({'message': 'put 요청입니다!'})
    
    def delete(self, request):
        """ 회원 정보를 삭제 합니다. """
        # is_active 변경하기 
        user = request.user
        user.is_active = False
        user.save()

        return Response({'message': 'delete 요청입니다!'})
    

class UserLoginView(APIView):
    def post(self, request):
        """ 로그인 기능입니다. """
        user = authenticate(**request.data)
        # is_active 체크하기 
        if not user:
            return Response({'message': '잘못된 비밀번호 혹은 존재하지 않는 사용자입니다.'})
        login(request, user)
        return Response({'message': '로그인 성공'})
    

class UserLogoutView(APIView):
    def post(self, request):
        """ 로그아웃 기능입니다. """
        logout(request)
        return Response({'message': '로그아웃 요청입니다!'})