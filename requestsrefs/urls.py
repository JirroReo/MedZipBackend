from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import re_path
from .views import (
    RequestRetrieveUpdateAPIView,
    RequestListAPIView,
    RequestCreateAPIView,
    SingleRequestListAPIView,
    AcceptRejectRetrieveUpdateAPIView,
    AcceptRejectListAPIView,
    AcceptRejectCreateAPIView,
    TransactionRetrieveUpdateAPIView,
    TransactionListAPIView,
    TransactionCreateAPIView,
)

urlpatterns = format_suffix_patterns([
    re_path(
        r'^(?P<pk>\d+)/$',
        RequestRetrieveUpdateAPIView.as_view(),
        name='get_or_update_request'
    ),
    re_path(
        r'^all$',
        RequestListAPIView.as_view(),
        name='get_all_requests'
    ),
    re_path(
        r'^create$',
        RequestCreateAPIView.as_view(),
        name='create_new_request'
    ),
    re_path(
        r'^details$',
        SingleRequestListAPIView.as_view(),
        name='get_single_request'
    ),


    # urls for accept reject table

    # update
    re_path(
        r'^accept/(?P<pk>\d+)/$',
        AcceptRejectRetrieveUpdateAPIView.as_view(),
        name='get_or_update_accept_reject'
    ),

    # list all
    re_path(
        r'^accept/all$',
        AcceptRejectListAPIView.as_view(),
        name='get_all_accept_reject'
    ),

    # create
    re_path(
        r'^accept/create$',
        AcceptRejectCreateAPIView.as_view(),
        name='create_new_accept_reject'
    ),

    # Transaction Table URLS

    # update a specific record
    re_path(
        r'^transaction/(?P<pk>\d+)/$',
        TransactionRetrieveUpdateAPIView.as_view(),
        name="get_or_update_transaction"
    ),
    # list all record from the table
    re_path(
        r'^transaction/all$',
        TransactionListAPIView.as_view(),
        name='get_all_transactions',
    ),
    # create new record
    re_path(
        r'^transaction/create$',
        TransactionCreateAPIView.as_view(),
        name='create_new_transaction'
    ),


])
