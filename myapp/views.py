from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import EmpSerializer
from .models import Employee

class MyApiView(APIView):
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = EmpSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, *args, **kwargs):

        qs = Employee.objects.all()

        serializer = EmpSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ReadUpdateView(APIView):
    def delete(self, *args, **kwargs):
        id = kwargs.get('id')
        shop = Employee.objects.get(pk=id)
        shop.delete()
        return Response("ok", status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        id = kwargs.get('id')
        data = self.request.data
        instance = Employee.objects.get(pk=id)
        serializer = EmpSerializer(instance=instance, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        # return Response({"msg": "office updated"})
        return Response(serializer.data, status.HTTP_200_OK)