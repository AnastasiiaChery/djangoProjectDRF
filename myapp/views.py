from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import ShopSerializer
from .models import Shop

class MyApiView(APIView):
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = ShopSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, *args, **kwargs):
        fil = self.request.query_params.get('filter', None)
        qs = Shop.objects.all()
        if fil:
            if fil==int:
                qs = qs.filter(id=int(fil))
            else:
                qs = qs.filter(name__startswith=str(fil))
        serializer = ShopSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        fil = self.request.query_params.get('filter', None)
        shop = Shop.objects.get(pk=fil)
        data = self.request.data
        serializer = ShopSerializer(shop, data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)