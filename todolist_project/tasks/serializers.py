from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task, Profile

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('gender', 'date_of_birth')

class UserRegistrationSerializer(serializers.ModelSerializer):
    gender = serializers.ChoiceField(choices=Profile.GENDER_CHOICES, write_only=True, required=True)
    date_of_birth = serializers.DateField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'gender', 'date_of_birth')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = {
            'gender': validated_data.pop('gender'),
            'date_of_birth': validated_data.pop('date_of_birth')
        }
        user = User.objects.create_user(**validated_data)
        user.profile.gender = profile_data['gender']
        user.profile.date_of_birth = profile_data['date_of_birth']
        user.profile.save()
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('username', 'email', 'profile')

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        profile = instance.profile
        profile.gender = profile_data.get('gender', profile.gender)
        profile.date_of_birth = profile_data.get('date_of_birth', profile.date_of_birth)
        profile.save()
        return instance