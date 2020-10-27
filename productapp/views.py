from django.shortcuts import render
from .models import Brand, Product
from rest_framework.viewsets import ModelViewSet
from .serializer import BrandSerializer, ProductSerializer
from rest_framework.response import Response

class BrandOps(ModelViewSet):
    """

         list:
             Return all Inactive Brands, ordered by mostly joined.

     """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(active= False)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)




class ProductOps(ModelViewSet):
    """
         retrive:
           return a Product instance.

         list:
             Return all Products, ordered by mostly joined & which “stockavailable” is less than or equal to the “reorderqty”.

         create:
             Create a new Product.

         delete:
             Delete an existing Product.

         partial_update:
             Update one or more fields on an existing Product which price is more than 10000.

         update:
             Update a Product which price is more than 10000.
     """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(stockavailable__lte = Product.reorderqty)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if 'price ' in request.data and int(request.data['price']) >= 10000:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)


            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        else:
            Response('Price Should Be Greater than 10000')
