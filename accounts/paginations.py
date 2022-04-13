from rest_framework.pagination import PageNumberPagination

class AccountPageNumberPagination(PageNumberPagination):
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 12
    page_size = 12

    def paginate_queryset(self, queryset, request, view=None):
        if request.query_params.get('all'):
            return None

        return super(AccountPageNumberPagination, self).paginate_queryset(
            queryset,
            request,
            view=view,
        )
