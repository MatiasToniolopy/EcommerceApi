from datetime import datetime
from re import T
from django.contrib.sessions.models import Session
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializer import UserTokenSerializer



class UserToken(APIView):
    
    def get(self, request, *args, **kwargs):
        username = request.GET.get('username')
        try:
            user_token = Token.objects.get(
                user = UserTokenSerializer().Meta.model.objects.filter(username = username).first()
            )
            return Response({'token': user_token.key})
        except:
            return Response ({'error': 'Credenciales enviadas incorrectas'}, status = status.HTTP_400_BAD_REQUEST)


class Login(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        
        login_serializer = self.serializer_class(data = request.data, context = {'request': request})
        
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token,create = Token.objects.get_or_create(user=user)
                user_serializer = UserTokenSerializer(user)
                if create:
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'inicio de sesion correcto'
                    }, status = status.HTTP_201_CREATED)
                else:
                    token.delete()
                    return Response({'error': 'ya se ha iniciado sesion con este usuario'}, status = status.HTTP_409_CONFLICT)
                    
            else:
                return Response({'message': 'este usuario no puede iniciar sesion'}, status = status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'usuario o contraseña incorrecta'}, status = status.HTTP_400_BAD_REQUEST)
        
    
            

class Logout(APIView):
    
    def get(self, request, *args, **kwargs):
        token = self.request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        
        if token:
            user = token.user
            
            all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
            if all_sessions.exists():
                for session in all_sessions:
                    session_data = session.get_decoded()
                    if user.id == int(session_data.get('_auth_user_id')):
                        session.delete()
            
            token.delete()
            
            session_message = 'sesiones de usuario elimiandas'
            token_message = 'token eliminado'
            return Response ({'token_message': token_message, 'session_message': session_message}, status = status.HTTP_200_OK)
        
        return Response ({'error': 'no se ha encontrado un usuario con estas credenciales'}, status = status.HTTP_400_BAD_REQUEST)