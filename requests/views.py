from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.generics import (
  RetrieveUpdateAPIView,
  ListAPIView,
  CreateAPIView,
  UpdateAPIView
)
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Request
from .serializers import RequestSerializer
from .paginations import LargePageNumberPagination

class RequestRetrieveUpdateAPIView(RetrieveUpdateAPIView):
  model = Request
  serializer_class = RequestSerializer
  pagination_class = LargePageNumberPagination

  def get(self, *args, **kwargs):
    response = super(RequestRetrieveUpdateAPIView, self).get(self.request, *args, **kwargs)


    return response

  def get_queryset(self):
    return self.model.objects.all().order_by('request_num')

class RequestListAPIView(ListAPIView):
  model = Request
  serializer_class = RequestSerializer
  search_fields = ('name', 'company', 'reason', 'findings', )

  def get_queryset(self):
    ordering = self.request.query_params.get('ordering', 'request_num')
    qs = self.model.objects.all()
    return qs.order_by(ordering).distinct()
