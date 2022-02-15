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
        
''' class TestUserSerializer(serializers.Serializer):
    
        name = serializers.CharField(max_length=255)
        email = serializers.EmailField()
        
        def validate_name(self, value):
            if 'developer' in value:
                raise serializers.ValidationError('ERROR, EL USUARIO NO PUEDE TENER ESE NOMBRE')
                
            return value
        
        def validate_email(self, value):
            if value == '':
                raise serializers.ValidationError('TIENE QUE INDICAR UN CORREO')
          
            return value
        
        def validate(self, data):
            
            return data
        
        def create(self, validate_data):
            print(validate_data)
            return User.objects.create(**validate_data)
        
        def update(self, instance, validate_data):
            instance.name = validate_data.get('name', instance.name)
            instance.email = validate_data.get('email', instance.email)
            instance.save()
            return instance '''