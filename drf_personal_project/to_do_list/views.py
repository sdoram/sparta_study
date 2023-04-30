from .models import ToDoList
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from .serializers import  ToDoListSerializer, ToDoListDetailSerializer, ToDoListCreateSerializer

class ToDoListView(APIView):
    def get(self, request):
        to_do_lists = ToDoList.objects.all()
        serializer = ToDoListSerializer(to_do_lists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
        # to do list 생성 
    def post(self, request):
        serializer = ToDoListCreateSerializer(data=request.data)
        # if문 없이 raise_exception을 사용하면 알아서 상태메시지까지 전달
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    


class ToDoListDetailView(APIView):
    def get(self, request,id):
        to_do_list = get_object_or_404(ToDoList, id=id)
        serializer = ToDoListSerializer(to_do_list)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        # to do list 수정 
        # 현재 제목이 필수사항 제목 입력 없이 is_complete 작성 가능해야함
        to_do_list = get_object_or_404(ToDoList, id=id)
        if request.user == to_do_list.user:
            serializer = ToDoListDetailSerializer(to_do_list, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message":"본인이 아닙니다"}, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, id):
        # to do list DELETE
        to_do_list = get_object_or_404(ToDoList, id=id)
        if request.user == to_do_list.user:
            to_do_list.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({"message":"본인이 아닙니다"}, status=status.HTTP_403_FORBIDDEN)