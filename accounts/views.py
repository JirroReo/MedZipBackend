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
from rest_framework.permissions import AllowAny

from .models import Account
from .serializers import AccountSerializer
from .paginations import AccountPageNumberPagination

class AccountRetrieveUpdateAPIView(RetrieveUpdateAPIView):
  model = Account
  serializer_class = AccountSerializer

  def get(self, *args, **kwargs):
    response = super(AccountRetrieveUpdateAPIView, self).get(self.request, *args, **kwargs)

    return response

  def get_queryset(self):
    searchbyuname = self.request.query_params.get('username')
    qs = self.model.objects.filter(is_active=True)
    if searchbyuname:
      qs = qs.filter(username = searchbyuname)
      
    return qs
    # return self.model.objects.filter(is_active=True)

class AccountListAPIView(ListAPIView):
  model = Account
  serializer_class = AccountSerializer
  pagination_class = AccountPageNumberPagination

  def get_queryset(self):
    ordering = self.request.query_params.get('ordering', 'id')
    qs = self.model.objects.filter(is_active=True)
    return qs.order_by(ordering).distinct()

class AccountCreateAPIView(CreateAPIView):
  permission_classes = ([AllowAny])

  model = Account
  serializer_class = AccountSerializer

