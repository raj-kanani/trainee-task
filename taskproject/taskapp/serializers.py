from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
from datetime import date

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD, 'full_name', 'is_active')


class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = ['number', 'status', 'start_date', 'end_date']

    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError({"end_date": "please enter future date in end date"})
        return data


class TaskSerializer(serializers.ModelSerializer):
    """status_display is a read-only field
     to be serialized that returns the value of the
     get_status_display method on the serializer"""

    # status = serializers.SerializerMethodField('get_status_display')

    class Meta:
        model = Task
        fields = ['id', 'task_number', 'description',
                  'sprint', 'user', 'status', 'start_date', 'image', 'backlog']

    # def get_status_display(self, obj):
    #     return obj.get_status_display()

