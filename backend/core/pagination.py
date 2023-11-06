from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PagePagination(PageNumberPagination):
    page_size = 5
    max_page_size = 15
    page_query_param = "page"

    def get_paginated_response(self, data):
        return Response(
            {
                "total_pages": self.page.paginator.count,
                "next": True if self.get_next_link() else False,
                "prev": True if self.get_previous_link() else False,
                "data": data,
            }
        )
