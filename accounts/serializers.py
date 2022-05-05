from rest_framework import serializers
from sorl.thumbnail import get_thumbnail

from .models import Account

class AccountSerializer(serializers.ModelSerializer):
  prc_pic_url = serializers.SerializerMethodField()

  class Meta:
    model = Account
    fields = (
      'id',
      'full_name',
      'email',
      'user_type',
      'contact_no',
      'birthday',
      'sex',
      'pronouns',
      'provider_type',
      'prc_num',
      'prc_pic_url'
    )

  def get_prc_pic_url(self, obj):
    if obj.prc_pic:
      if obj.prc_pic.width > 220:
        picture = get_thumbnail(obj.prc_pic, '220', quality=85)
      else:
        picture = get_thumbnail(
          obj.prc_pic,
          '{}'.format(obj.prc_pic.width),
          quality=90
        )

      return picture.url
class CreateAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"

class ChangePasswordSerializer(serializers.ModelSerializer):
  class Meta:
    model = Account
    fields = "__all__"

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

