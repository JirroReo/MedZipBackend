from django.contrib import admin
from .models import Request

class RequestAdmin(admin.ModelAdmin):
  model = Request
  readonly_fields = ('request_num', )
  list_display = ('request_num', 'reason', 'name', )
  search_fields = (
    'request_num', 
    'name', 
    'company', 
    'findings', 
  )

admin.site.register(Request, RequestAdmin)
