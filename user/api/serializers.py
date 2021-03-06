from dataclasses import field
from tkinter.ttk import Style
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerealizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password")


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ("username", "email", "password", "password2")
        extra_kwargs = {
            "password": {
                'write_only': True
            }
        }
