from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import re_path
from .views import (
  RequestRetrieveUpdateAPIView,
  RequestListAPIView,
  RequestCreateAPIView,
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
  )
])                                                                        
