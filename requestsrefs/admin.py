from django.contrib import admin
from .models import RequestRef, AcceptRejectModel, TransactionModel

class RequestAdmin(admin.ModelAdmin):
  model = RequestRef
  readonly_fields = ('request_num', )
  list_display = ('request_num', 'reason', 'name', )
  search_fields = (
    'request_num', 
    'name', 
    'company', 
    'findings', 
  )

admin.site.register(RequestRef, RequestAdmin)
admin.site.register(AcceptRejectModel)
admin.site.register(TransactionModel)
