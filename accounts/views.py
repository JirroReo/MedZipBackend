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
from .serializers import  CreateAccountSerializer
from .serializers import ChangePasswordSerializer
from .paginations import AccountPageNumberPagination

from rest_framework.permissions import IsAuthenticated 

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
  serializer_class = CreateAccountSerializer

class SingleAccountListAPIView(ListAPIView):
  model = Account
  serializer_class = AccountSerializer
  # pagination_class = AccountPageNumberPagination

  def get_queryset(self):
    emailparam = self.request.query_params.get('email', None)
    ordering = self.request.query_params.get('ordering', 'id')
    qs = self.model.objects.filter(is_active=True)
    if emailparam is not None:
      qs = qs.filter(email=emailparam)
    return qs

class ChangePasswordView(UpdateAPIView):
        """
        An endpoint for changing password.
        """
        serializer_class = ChangePasswordSerializer
        model = Account
        permission_classes = (IsAuthenticated,)

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }

                return Response(response)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
