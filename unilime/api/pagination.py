from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class ReviewPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response(
            {
                "count": self.page.paginator.count,
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "reviews": data,
            }
        )
