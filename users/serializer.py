from rest_framework import serializers
from .models import User

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'last_name')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
    def create(self, validate_data):
        user = User(**validate_data)
        user.set_password(validate_data['password'])
        user.save()
        return user
    
    def update(self, instance, validate_data):
        user_update = super().update(instance, validate_data)
        user_update.set_password(validate_data['password'])
        user_update.save()
        return user_update

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
                
    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email'],
            'password': instance['password']
        }
