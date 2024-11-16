from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from core.serializers import (ProductSerializer, LLMSerializer, PathSerializer, PromptSerializer, DateSerializer, 
                              UserRegistrationSerializer, UserSerializer)
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
import xml.etree.ElementTree as ET
from core.utils import  generate_report, analytical_report, lst_products, insert_data
from core.models import Product, AnswerLLm, User
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import status
from core.serializers import  MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class UserViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    '''Вьюшка создания пользователя и получения списков пользователей'''
    queryset = User.objects.all()
    permission_classes = [AllowAny,]

    def get_permissions(self):  
        if self.action == 'create':  
            permission_classes = [AllowAny,]  
        else:  
            permission_classes = [IsAuthenticated,]  
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'create':
           return UserRegistrationSerializer
        return UserSerializer


class ProductView(ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated,]
    queryset = Product.objects.all()

class LLMView(ReadOnlyModelViewSet):
    serializer_class = LLMSerializer
    permission_classes = [IsAuthenticated,]
    queryset = AnswerLLm.objects.all().order_by('-id')


class ParseXmlView(APIView): 
    serializer_class = PathSerializer
    permission_classes = [IsAuthenticated,]

    def post(self,request):
        # path = request.GET.get('arg')     
        path = PathSerializer(request.data).data['path']  
        data = lst_products(path)      
        insert_data(data)

        return Response({'res':'The data has been added successfully'})
    
    
class AnalyzeView(APIView):
    serializer_class = DateSerializer
    permission_classes = [IsAuthenticated,]
    def post(self, request):
        date_product = DateSerializer(request.data).data['date_product']       
        result = generate_report(date_product)

        return Response(result)
    
    
class AnalyticalReport(APIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = PromptSerializer
    def post(self, request):
        user = request.user
        prompt = PromptSerializer(request.data).data['prompt']
        res = analytical_report(prompt).strip('\n')
        
        AnswerLLm.objects.create(user=user,prompt=prompt,answer=res)

        return Response({'res': res})


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer