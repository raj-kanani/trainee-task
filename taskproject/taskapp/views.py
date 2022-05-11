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
    queryset = Sprint.objects.all()
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


# move to expire (inactive) to active sprint
class MoveTask(APIView):
    def post(self, request):
        data = request.data
        sprint = Sprint.objects.get(status=data['status'])
        if sprint.status != "active":
            sprint.status = "active"
            sprint.save()
        return Response({'success': 'task successfully moved'})


# change the status of task
class ChangeStatus(APIView):
    def post(self, request):
        data = request.data
        task = Task.objects.get(status=data['status'])
        if task.status != "STATUS_COMPLETED":
            task.status = "STATUS_COMPLETED"
            task.save()
        return Response({'msg': 'status updated'})


# move task from backlog to active sprint.
class MoveBacklog(APIView):
    def post(self, request, id):
        data = request.data
        task = Task.objects.get(id=data['id'])
        print(task)
        if task.backlog:
            print(task.backlog)
            print(task.sprint.status, '*************')
            task.sprint.status = "active"
            task.save()
            print(task.sprint.status, '*************')
        return Response({'msg': 'success !!! move backlog to active sprint'})
