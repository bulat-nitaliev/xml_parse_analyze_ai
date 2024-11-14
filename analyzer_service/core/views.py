from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from core.serializers import ProductSerializer
import xml.etree.ElementTree as ET
from core.utils import  generate_report, analytical_report, lst_products, insert_data
from core.models import Product, AnswerLLm
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated



class ProductView(ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated,]
    queryset = Product.objects.all()


class ParseXmlView(APIView): 
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated,]

    def get(self,request):
        path = request.GET.get('arg')       
        
        data = lst_products(path)
        
        insert_data(data)

        return Response({'res':'The data has been added successfully'})
    
class AnalyzeView(APIView):
    def get(self, request):
        date_product = request.GET.get('arg')  
        print(date_product)
        result = generate_report(date_product)

        return Response(result)
    
class AnalyticalReport(APIView):
    def get(self, request):
        prompt = request.GET.get('arg')
        res = analytical_report(prompt).strip('\n')
        print(res)
        AnswerLLm.objects.create(answer=res)

        return Response({'res': res})

