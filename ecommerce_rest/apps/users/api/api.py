from rest_framework.views import APIView
from rest_framework import status
from apps.users.api.serializers import UserSerializer, UserListSerializer
from apps.users.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def user_api_view(request):
    if request.method == "GET":
        users = User.objects.all().values('id', 'username', 'email', 'password')
        #'usando many el serializador sabe que son varios valores y no uno'
        users_serializers = UserListSerializer(users, many = True)
        return Response(users_serializers.data, status = status.HTTP_200_OK)
    elif request.method == "POST":
        #aca lo que hace el serializador es almacenar el json que es retornado
        #usando usando el modulo request y el metodo data, para obtener esa info
        user_serializer = UserSerializer(data = request.data)
        #si la info pasa el filtro de validacion del modelo, se guarda
        if user_serializer.is_valid():     
            user_serializer.save()
            return Response(user_serializer.data, status = status.HTTP_201_CREATED)
        #de lo contrario devuelve el mensaje de manejo de errores en el modelo
        return Response(user_serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk=None):
    user = User.objects.filter(id = pk).first()

    if user:
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status = status.HTTP_200_OK)
        
        elif request.method == 'PUT':
            user_serializer = UserSerializer(user, data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data)
            return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            user.delete()
            return Response({'message':'usuario eliminado correctamente!'}, status = status.HTTP_200_OK)
    return Response({'message':'No se ha encontrado usuario con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)