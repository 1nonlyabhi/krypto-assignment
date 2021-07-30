from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        # password = validated_data.pop('password', None)
        # if password is not None:
        user = User()
        user.set_password(validated_data['password'])
        validated_data['password'] = user.password
        return super().create(validated_data)