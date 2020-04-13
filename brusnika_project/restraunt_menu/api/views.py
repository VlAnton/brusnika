from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.authentication import SessionAuthentication

from restraunt_menu.models import MenuItem
from restraunt_menu.api.serializers import MenuItemSerializer


class MenuAPIView(ListCreateAPIView):
    serializer_class = MenuItemSerializer
    authentication_classes = [SessionAuthentication]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
