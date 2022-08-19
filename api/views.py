from django.shortcuts import render
from .models import Property, StatusHistory
from rest_framework import viewsets
from django.db.models import Prefetch
from rest_framework.decorators import action
from .serializers import PropertyListSerializer, StatusHistoryListSerializer
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 1000

class PropertyListView(viewsets.ModelViewSet):
    http_method_names = ['get', 'head']
    serializer_class = PropertyListSerializer
    queryset = Property.objects.all()
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return PropertyListSerializer
        return PropertyListSerializer

    def get_queryset(self):
        queryset = Property.objects.all()
        '''
        queryset = Property.objects.prefetch_related(Prefetch(
        'status'))
        '''

        if self.request.GET.get('year'):
            queryset = queryset.filter(year=self.request.GET.get('year'))
        if self.request.GET.get('city'):
            queryset = queryset.filter(city=self.request.GET.get('city'))
        else:
            queryset = queryset.order_by('-year')
        return queryset
    
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
            
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)