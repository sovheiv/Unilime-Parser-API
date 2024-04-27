from api.pagination import ReviewPagination
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Product, Review
from .serializers import ProductSerializer, ReviewSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ["get"]

    @method_decorator(cache_page(100))
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        reviews = instance.reviews.all()
        paginator = ReviewPagination()
        paginated_reviews = paginator.paginate_queryset(reviews, request)

        serialized_product = serializer.data

        if paginated_reviews is not None:
            serialized_reviews = ReviewSerializer(paginated_reviews, many=True)
            response_data = paginator.get_paginated_response(
                serialized_reviews.data
            ).data
            response_data["product"] = serialized_product
            return Response(response_data)

        return Response(serialized_product)


class ReviewViewSet(viewsets.ModelViewSet):
    http_method_names = ["post"]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
