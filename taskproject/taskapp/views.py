from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework import authentication, permissions, viewsets
from django.contrib.auth import get_user_model


class DefaultsMixin(object):
    authentication_classes = (authentication.BasicAuthentication,
                              authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)


class SprintViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = Sprint.objects.order_by('end_date')
    serializer_class = SprintSerializer


class TaskViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


User = get_user_model()


class UserViewSet(DefaultsMixin, viewsets.ModelViewSet):
    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer


class MoveTask(APIView):
    def post(self, request):
        data = request.data
        sprint = Sprint.objects.get(status=data['status'])
        if sprint.status != "active":
            sprint.status = "active"
            sprint.save()
        return Response({'success': 'task successfully moved'})


class ChangeStatus(APIView):
    def post(self, request):
        data = request.data
        task = Sprint.objects.get(status=data['status'])
        task.status = data['status']
        task.save()
        return Response({'msg': 'status updated'})


