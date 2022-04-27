from django.shortcuts import render
from rest_framework.generics import (
    RetrieveUpdateAPIView,
    ListAPIView,
    CreateAPIView,
)

from .models import RequestRef, AcceptRejectModel, TransactionModel
from .serializers import RequestSerializer, AcceptRejectSerializer, TransactionSerializer
from .paginations import LargePageNumberPagination


class RequestRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    model = RequestRef
    serializer_class = RequestSerializer
    pagination_class = LargePageNumberPagination

    def get(self, *args, **kwargs):
        response = super(RequestRetrieveUpdateAPIView, self).get(
            self.request, *args, **kwargs)

        return response

    def get_queryset(self):
        return self.model.objects.all().order_by('request_num')


class RequestListAPIView(ListAPIView):
    model = RequestRef
    serializer_class = RequestSerializer
    search_fields = ('name', 'company', 'reason', 'findings', )

    def get_queryset(self):
        ordering = self.request.query_params.get('ordering', 'request_num')
        qs = self.model.objects.all()
        return qs.order_by(ordering).distinct()


class RequestCreateAPIView(CreateAPIView):
    model = RequestRef
    serializer_class = RequestSerializer

    def create(self, request, **kwargs):
       
        response = super(RequestCreateAPIView, self).create(request, **kwargs)
        return response

class SingleRequestListAPIView(ListAPIView):
  model = RequestRef
  serializer_class = RequestSerializer

  def get_queryset(self):
    accid = self.request.query_params.get('accid')
    qs = RequestRef.objects.filter(account__pk=accid)
    ordering = self.request.query_params.get('ordering', 'request_num')
    if qs is not None:
        return qs
    else:
        data['message'] = 'No records found'
        return data

# API FOR THE ACCEPT REJECT TABLE

# to update the record


class AcceptRejectRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    model = AcceptRejectModel
    serializer_class = AcceptRejectSerializer
    pagination_class = LargePageNumberPagination

    def get(self, *args, **kwargs):
        response = super(AcceptRejectRetrieveUpdateAPIView,
                         self).get(self.request, *args, **kwargs)
        return response

    def get_queryset(self):
        return self.model.objects.all().order_by('entry_num')


# to view the all records in table
class AcceptRejectListAPIView(ListAPIView):
    model = AcceptRejectModel
    serializer_class = AcceptRejectSerializer

    def get_queryset(self):
        ordering = self.request.query_params.get('ordering', 'entry_num')
        qs = self.model.objects.all()
        return qs.order_by(ordering).distinct()


# to create new record
class AcceptRejectCreateAPIView(CreateAPIView):
    model = AcceptRejectModel
    serializer_class = AcceptRejectSerializer

    def create(self, request, **kwargs):
        response = super(AcceptRejectCreateAPIView,
                         self).create(request, **kwargs)
        return response

# API FOR THE TRANSACTION TABLES
class TransactionRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    model = TransactionModel
    serializer_class = TransactionSerializer
    pagination_class = LargePageNumberPagination

    def get(self, *args, **kwargs):
        response = super(TransactionRetrieveUpdateAPIView,
                         self).get(self.request, *args, **kwargs)
        return response

    def get_queryset(self):
        return self.model.objects.all().order_by('date')



# to view the all records in table
class TransactionListAPIView(ListAPIView):
    model = TransactionModel
    serializer_class = TransactionSerializer

    def get_queryset(self):
        ordering = self.request.query_params.get('ordering', 'date')
        qs = self.model.objects.all()
        return qs.order_by(ordering).distinct()

# to create new record
class TransactionCreateAPIView(CreateAPIView):
    model = TransactionModel
    serializer_class = TransactionSerializer

    def create(self, request, **kwargs):
        response = super(TransactionCreateAPIView, self).create(request, **kwargs)
        return response