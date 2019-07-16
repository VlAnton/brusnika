from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from ..models import MenuItem
from ..serializers import MenuItemSerializer


class MenuAPIView(ListCreateAPIView):
    queryset = MenuItem.items.all()
    serializer_class = MenuItemSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get(self, request):
        serializer = self.serializer_class(self.get_queryset(), many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
