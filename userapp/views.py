from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class UserAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            'status': 200,
            'message': 'ok',
        })