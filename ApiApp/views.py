from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import FoodSerializer
from .models import Food

class FoodViewSet(viewsets.ModelViewSet):
    #查詢所有產品 按 name 排序
    queryset = Food.objects.all().order_by('p_name')
    serializer_class = FoodSerializer