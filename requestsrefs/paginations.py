from rest_framework.pagination import PageNumberPagination

class SmallPageNumberPagination(PageNumberPagination):
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_size = 10

    def paginate_queryset(self, queryset, request, view=None):
        if request.query_params.get('all'):
            return None

        return super(SmallPageNumberPagination, self).paginate_queryset(
            queryset,
            request,
            view=view,
        )


class LargePageNumberPagination(PageNumberPagination):
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 500
    page_size = 20

    def paginate_queryset(self, queryset, request, view=None):
        if request.query_params.get('all'):
            return None

        return super(LargePageNumberPagination, self).paginate_queryset(
            queryset,
            request,
            view=view,
        )


