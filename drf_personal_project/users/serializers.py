from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
    
    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        # 비밀번호 해싱
        user.set_password(password)
        user.save()
        return user
    

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email","password","name","gender","age","introduction"]
        extra_kwargs = {
            "password": {'write_only': True},
            "email":{'read_only' : True},
        }
    

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        token['name'] = user.name
        token['gender'] = user.gender
        token['age'] = user.age
        # ...

        return token