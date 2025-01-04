from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password", "date_joined")

        extra_kwargs = {"password": {"write_only": True}, "date_joined": {"read_only": True}}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance is not None:
            self.fields["password"].required = False

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if "password" in validated_data:
            validated_data["password"] = make_password(validated_data.get("password"))
        return super().update(instance, validated_data)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("user", "name", "description", "status", "created_at")

        extra_kwargs = {"user": {"read_only": True}, "created_at": {"read_only": True}}
