from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django.core import serializers


from .serializers import UserSerializer, ActivityPeriodSerializer, TimelineSerializer
from .models import User, ActivityPeriod
from django.http import JsonResponse
from django.views.generic import ListView

from django.shortcuts import render
from django.core import serializers
from rest_framework.response import Response
from django.http import HttpResponse
from .models import User
import json
from rest_framework.decorators import api_view

from rest_framework.views import APIView

from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from collections import namedtuple

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ActivityPeriodViewSet(viewsets.ModelViewSet):
    queryset = ActivityPeriod.objects.all()
    serializer_class = ActivityPeriodSerializer

class TimelineViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing the Tweets and Articles in your Timeline.
    """
    def list(self, request):
        Timeline = namedtuple('Timeline', ('ok', 'members'))
        timeline = Timeline(
            ok=True,
            members=User.objects.all(),
        )
        serializer = TimelineSerializer(timeline, context={'request': request})
        return Response(serializer.data)