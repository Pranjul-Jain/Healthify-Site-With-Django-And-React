from rest_framework import serializers
from django.contrib.auth.models import User
from Models.models import healthtips


class HealthtipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = healthtips
        fields = ['tips', 'tip_description']


class adminSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    username = serializers.CharField(
        write_only=True,
        required=True,
        style={'placeholder': "Username"}
    )

    class Meta:
        model = User
        fields = ['username', 'password']
