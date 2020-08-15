from django.shortcuts import render
from rest_framework import generics
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import create_user, create_event
from .serializers import UserSerializer, EventSerializer
from . import serializers
from django.http import Http404

class event_list(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user.id
        eventos = create_event.objects.filter(event_user=user)
        serializer = serializers.EventSerializer(eventos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class event_detail(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, evento_id):
        user = request.user.id
        eventos = create_event.objects.filter(event_user=user, id=evento_id)
        serializer = serializers.EventSerializer(eventos, many=True)
        return Response(serializer.data)

    def put(self, request, evento_id):
        user = request.user.id 
        eventos = create_event.objects.get(event_user=user, id=evento_id)
        serializer = serializers.EventSerializer(eventos, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            eventos_arc = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, evento_id):
        try:
            eventos = create_event.objects.get(id=evento_id)
        except create_event.DoesNotExist:
            raise Http404
        eventos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)