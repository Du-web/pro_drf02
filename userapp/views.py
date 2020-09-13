from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from userapp.models import User


class UserAPIView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        name = request.GET.get('username')
        print(id, name)
        print(request.query_params)
        print(request.query_params.get('username'))
        if id:
            user = User.objects.filter(pk=id).values('name', 'pwd', 'gender').first()
            if user:
                return Response({
                    'status': 200,
                    'message': 'ok',
                    'results': user
                })
            else:
                return Response({
                    'status': 500,
                    'message': '用户不存在 ',

                })
        else:
            users = User.objects.all().values('name', 'pwd', 'gender')
            return Response({
                'status': 200,
                'message': 'ok',
                'results': list(users)
            })