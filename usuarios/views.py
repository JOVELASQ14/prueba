from django.shortcuts import render
from .serializers import UserProfileSerializers
from .models import UserProfile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt

# Create your views here.
class RegisterUser(APIView):
    def post(self, request):
        user_serialized = UserProfileSerializers(request.data)
        user_serialized.is_valid(raise_exception=True)
        user_serialized.save()
        return Response(user_serialized.data) 


class LoginUser(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        log_user = UserProfile.objects.filter(email=email).first()
         
        if log_user is None:
            raise AuthenticationFailed("El usuario no existe")
        
        if not log_user.check_password(raw_password=password):
            raise AuthenticationFailed("Contraseña incorrecta")

        # JWT
        payload = {
            "name": log_user.name,
            "age": log_user.age,
            "gender": log_user.genre,
            "cc": log_user.cc,
            "phone_number": log_user.phone_number,
            "email": log_user.email
        }

        token = jwt.encode(payload=payload, key='token', algorithm='HS256')

        response = Response()

        # response.set_cookie(key="jwt", value="token", httponly=True)

        response.data = {
            "secret": token
        }

        return response
    

class LogOutUser(APIView):
    def post(self, request):
        response = Response()
        response.data = {
            "message": "Sesión cerrada" 
        }




