from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import DevelopersSeriallizer
from . models import Developers

# Create your views here.

class DevelopersApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):

    serializer_class = DevelopersSeriallizer
    queryset = Developers.objects.all()
    lookup_field = 'id'
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
         return self.list(request)

    def post(self,request):
         return self.create(request)


class DevelopersApiModifyView(generics.GenericAPIView,mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = DevelopersSeriallizer
    queryset = Developers.objects.all()
    lookup_field = 'id'
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)





