from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import re_path

from .views import (
  AccountRetrieveUpdateAPIView,
  AccountListAPIView
)

urlpatterns = format_suffix_patterns([
  re_path(
    r'^(?P<pk>\d+)/profile$',
    AccountRetrieveUpdateAPIView.as_view(),
    name='get_or_update_account'
  ),
  re_path(
    r'all$',
    AccountListAPIView.as_view(),
    name='get_all_accounts'
  )
])
