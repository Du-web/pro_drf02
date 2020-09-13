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

    def post(self, request, *args, **kwargs):
        print(request.POST.get('name'))
        print(request.POST.get('pwd'))
        name = request.data.get('name')
        pwd = request.data.get('pwd')
        print(name, pwd)
        print(request.data)
        try:
            user = User.objects.create(name=name, pwd=pwd)
            return Response({
                'status': 200,
                'message': 'ok',
                'results':{'username': user.name}
            })
        except:
            return Response({
                'status': 500,
                'message': '注册失败'
            })

    def put(self, request, *args, **kwargs):
        id = kwargs.get('id')
        name = request.query_params.get('name')
        pwd = request.GET.get('pwd')
        user = User.objects.filter(pk=id)
        try:
            user[0].name = name
            user[0].pwd = pwd
            user[0].save()
            return Response({
                'status': 200,
                'message': 'ok',
                'results': {'username': user[0].name}
            })
        except:
            return Response({
                'status': 500,
                'message': '更新失败',
            })

