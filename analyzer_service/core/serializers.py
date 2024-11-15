from rest_framework import serializers
from core.models import Product, AnswerLLm, User
from rest_framework import serializers
from typing import Any, Dict
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.exceptions import InvalidToken

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 
                  'date_product', 
                  'quantity',
                  'price',
                  'category'
                )
        

class LLMSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerLLm
        fields = ('prompt',
                  'answer',
                  'dt_create')
        
class PathSerializer(serializers.Serializer):
    path = serializers.CharField()

class PromptSerializer(serializers.Serializer):
    prompt = serializers.CharField()

class DateSerializer(serializers.Serializer):
    date_product = serializers.DateField()




class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "email",
            "first_name",
            "last_name"
        )
        extra_kwargs = {'password': {
            'write_only': True
        }}

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"]          
        )
        user.set_password(validated_data["password"])
        user.save()

        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name"
        )


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        data = super().validate(attrs)
        data['username'] = self.user.username
        return data
    
 