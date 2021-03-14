from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['location', 'phone_number', 'profile_pic']
        #fields = ['user', 'location', 'phone_number', 'profile_pic']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    user_profile = UserProfileSerializer()
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'password', 'email', 'groups', 'user_profile']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        userProfile_data = validated_data.pop('user_profile')
        user = User.objects.create_user(**validated_data)
        user.userProfile = UserProfile.objects.create(user=user, **userProfile_data)
        user.save()

        return user

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']