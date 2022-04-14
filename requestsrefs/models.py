from django.db import models
from accounts.models import Account

class RequestRef(models.Model):
  request_num = models.AutoField(
    primary_key=True,
    unique=True,
    editable=False,
  )

  REQUEST_TYPE_CHOICES = (
    ('PADR', 'Patient - Doctor'),
    ('PAPH', 'Patient - Pharmacist'),
    ('DRPH', 'Doctor - Pharmacist'),
    ('DRDR', 'Doctor - Doctor'),
    ('PHPH', 'Pharmacist - Pharmacist'),
  )
  request_type = models.CharField(
    max_length=4,
    choices=REQUEST_TYPE_CHOICES,
    default='PADR'
  )
  account = models.ForeignKey(Account, on_delete=models.CASCADE)
  company = models.CharField(
    max_length=255,
    null=True, blank=True,
  )
  reason_for_consultation = models.CharField(
    max_length=1024
  )
  appointment_date = models.DateField()
  findings = models.CharField(
    max_length=1024,
    null=True, blank=True
  )
  session = models.CharField(
    max_length=512,
    null=True, blank=True
  )
  request = models.CharField(
    max_length=512,
    null=True, blank=True
  )
  prescription = models.CharField(
    max_length=512,
    null=True, blank=True
  )

  @property
  def name(self):
    return self.account.full_name

  @property
  def reason(self):
    return self.reason_for_consultation or 'Unknown Reason'

  def __str__(self):
    return str(self.request_num) + ': ' + self.name
