from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PagePagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page'
    max_page_size = 10

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'prev': self.get_previous_link(),
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })
