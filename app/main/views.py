import base64
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView




# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(APIView):

    def post(self, request):
        # Your authentication logic here
        basic_token = base64.b64encode(f"{request.data['username']}:{request.data['password']}")
        return Response({'Basic': basic_token})


# Create your views here.
