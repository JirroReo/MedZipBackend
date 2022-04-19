from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

class Account(AbstractUser):
  username = None
  email = models.EmailField(
    verbose_name='email address',
    max_length=255,
    unique=True,
  )
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []
  # USERNAME_FIELD = 'email'
  USER_TYPE_CHOICES = (
    ('Patient', 'Patient'),
    ('Provider', 'Provider'),
  )
  user_type = models.CharField(
    max_length=20,
    choices=USER_TYPE_CHOICES,
    default='Patient'
  )
  seed_phrase = models.CharField(
    max_length=255,
    unique=True,
  )
  first_name = models.CharField(
    max_length=20,
    null=True, 
    blank=True,
  )
  last_name = models.CharField(
    max_length=20,
    null=True, 
    blank=True,
  )
  password = models.CharField(
    max_length=100,
    default='none'
  )
  contact_no = models.IntegerField(null=True, blank=True)
  birthday = models.DateField(null=True, blank=True)
  SEXES_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
  )
  sex = models.CharField(
    max_length=1,
    choices=SEXES_CHOICES,
    default='none'
  )
  pronouns = models.CharField(
    null=True, 
    blank=True,
    max_length=16
  )
  PROVIDER_CHOICES = (
    ('N/A', 'Not Applicable'),
    ('Doctor', 'Doctor'),
    ('Pharmacist', 'Pharmacist'),
  )
  provider_type = models.CharField(
    max_length=20,
    choices=PROVIDER_CHOICES,
    default='N/A'
  )
  prc_num = models.IntegerField(null=True, blank=True)
  prc_pic = models.ImageField(
    upload_to='assets/useruploads/images/',
    # height_field=80,
    # width_field=80,
    # max_length=100,
    null=True, blank=True,
  )

  class Meta:
    ordering = ['id', 'email', 'first_name', 'last_name']
  
  @property
  def full_name(self):
    return self.first_name + ' ' + self.last_name
 
  def save(self, *args, **kwargs):
    self.seed_phrase = make_password(self.seed_phrase)
    # Use check_password('Plain text input', self.seed_phrase) to verify if input correct
    super(Account, self).save(*args, **kwargs)
 
  def __str__(self):
    return '{} {} ({})'.format(
      self.first_name, 
      self.last_name, 
      self.email
    )
