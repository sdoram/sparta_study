from rest_framework import serializers
from .models import ToDoList


class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = "__all__"

    user = serializers.SerializerMethodField()
    def get_user(self, obj):
        return obj.user.email
    
    
class ToDoListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ["title"]

class ToDoListDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ["id", "title", "is_complete", "created_at", "completion_at"]
        extra_kwargs = {
            "created_at":{'read_only' : True},
            "updated_at":{'read_only' : True},
        }