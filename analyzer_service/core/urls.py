from django.urls import path
from core.views import ProductView, ParseXmlView, AnalyzeView, AnalyticalReport
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('product', ProductView, 'product')



urlpatterns = [
    path('parse_xml/', ParseXmlView.as_view()),
    path('report/', AnalyzeView.as_view()),
    path('analytical_report/' , AnalyticalReport.as_view()),
    
]

urlpatterns += router.urls