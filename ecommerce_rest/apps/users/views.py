from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from apps.users.api.serializers import UserTokenSerializer

# Create your views here.
class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        #obtenemos el serializador de la vista obtainAuth, a la hora de validar, los unicos campos que valida son
        #user and password
        login_serializer = self.serializer_class(data = request.data, context = {'request':request})

        if login_serializer.is_valid():
            print("Paso validacion!")
            user = login_serializer.validated_data['user']

            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                user_serializer = UserTokenSerializer(user)
                if created:
                    return Response({
                        'token':token.key,
                        'user':user_serializer.data,
                        'message': 'Inicio de sesion exitoso!'
                    }, status = status.HTTP_201_CREATED)
                else:
                    token.delete()
                    token = token.objects.create(user = user)
                    return Response({
                        'token':token.key,
                        'user':user_serializer.data,
                        'message': 'Inicio de sesion exitoso!'
                    }, status = status.HTTP_201_CREATED)
                #return Response({'Bienvenido': f'Bienvenido {user} una vez mas!'})
            else:
                return Response({'error':'este usuario no esta activo para iniciar sesion!'},status = status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'Error':'Nombre de usuario o contraseña Incorrecta'}, status=status.HTTP_401_UNAUTHORIZED )

        return Response({'mensaje':'hola desde response'}, status=status.HTTP_200_OK )
