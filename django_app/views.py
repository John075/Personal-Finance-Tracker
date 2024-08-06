from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json

from rest_framework import generics
from rest_framework.generics import ListAPIView

from django_app.UserSerializer import UserSerializer
from django_app.models import User


# Needs to include exporting raw data, assign types to transactions (think feedback logic), see metrics regarding user.
#
#
#

class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
