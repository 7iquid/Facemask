from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Machine, McRecordingArea
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'password']
#         extra_kwargs = {'password': {'write_only': True, 'required': True}}

#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         Token.objects.create(user=user)
#         return user

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields= '__all__'

class McRecordingAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = McRecordingArea
        # fields= '__all__'
        fields= [
        'root_cause',
        'action_taken',
        'remarks',
        'total_down_time',
        ]


