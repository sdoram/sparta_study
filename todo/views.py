from rest_framework.views import APIView
from rest_framework.response import Response


class TodoView(APIView):
    def get(self, request, pk=None):
        """ pk값의 유무에 따라 todo 목록 혹은 todo 의 상세 정보를 response 합니다. """

        return Response({'message': 'get 요청입니다!'})
    
    def post(self, request):
        """ 내용을 입력받아 todo를 생성합니다. """

        return Response({'message': 'post 요청입니다!'})
    
    def put(self, request):
        """ 내용을 입력받아 todo를 수정합니다. """

        return Response({'message': 'put 요청입니다!'})
    
    def delete(self, request):
        """ todo를 삭제 합니다. """

        return Response({'message': 'delete 요청입니다!'})
    

class ToDoCompleteView(APIView):
    def put(self, request):
        """ todo의 is_complete를 수정합니다. """

        return Response({'message': 'todo 완료'})
    