from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

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
    class Meta:
        model = Task
        fields = '__all__'
