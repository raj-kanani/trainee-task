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
