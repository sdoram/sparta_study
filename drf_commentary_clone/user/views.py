from rest_framework.views import APIView
from rest_framework.response import Response


class UserView(APIView):
    def get(self, request):
        """ 사용자 정보를 response 합니다. """

        return Response({'message': 'get 요청입니다!'})
    
    def post(self, request):
        """ 사용자 정보로 회원 가입 합니다. """

        return Response({'message': 'post 요청입니다!'})
    
    def put(self, request):
        """ 회원 정보를 수정 합니다. """

        return Response({'message': 'put 요청입니다!'})
    
    def delete(self, request):
        """ 회원 정보를 삭제 합니다. """

        return Response({'message': 'delete 요청입니다!'})
    

class UserLoginView(APIView):
    def post(self, request):
        """ 로그인 기능입니다. """
        
        return Response({'message': '로그인 요청입니다!'})
    

class UserLogoutView(APIView):
    def post(self, request):
        """ 로그아웃 기능입니다. """
        
        return Response({'message': '로그아웃 요청입니다!'})