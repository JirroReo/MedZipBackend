from rest_framework import serializers
from accounts.serializers import AccountSerializer

from .models import RequestRef

class RequestSerializer(serializers.ModelSerializer):
  account = AccountSerializer(read_only=True)

  class Meta:
    model = RequestRef
    depth = 2
    fields = (
      'request_num',
      'request_type',
      'name',
      'company',
      'reason',
      'appointment_date',
      'findings',
      'session',
      'request',
      'prescription',
      'account',
    )
