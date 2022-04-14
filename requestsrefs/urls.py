from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import re_path
from .views import (
  RequestRetrieveUpdateAPIView,
  RequestListAPIView
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
  )
])                                                                        
