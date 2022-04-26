from requests import request
from rest_framework import serializers
from accounts.models import Account
from hashid_field.rest import HashidSerializerCharField
from .models import RequestRef, AcceptRejectModel, TransactionModel


class RequestSerializer(serializers.ModelSerializer):
    account = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all())
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


# Serializer for Accept Reject Table
class AcceptRejectSerializer(serializers.ModelSerializer):
    request_num = serializers.PrimaryKeyRelatedField(
      
        queryset=RequestRef.objects.all())

    class Meta:
        model = AcceptRejectModel
        depth = 2
        fields = (
            'entry_num',
            'request_num',
            'date',
            'doctor_name',
            'recommendation',
            'summary',
            'explanation',
            'medical_order',
            'others',
            'status',

        )


# Serializer for Transaction Table
class TransactionSerializer(serializers.ModelSerializer):

    transaction_id = serializers.PrimaryKeyRelatedField(
        pk_field=HashidSerializerCharField(source_field='requestsrefs.AcceptRejectModel.entry_num'),
        queryset=AcceptRejectModel.objects.all())

    class Meta:
        model = TransactionModel
        depth = 2
        fields = (
            'transaction_id',
            'date',
            'summary',
            'from_p',
            'to',
        )
