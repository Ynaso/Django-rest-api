from rest_framework import generics


#la clase generics sirve para poder mostrar views de los serializadores, asi evitamos usar un filter y retornarlo con el ORM
#de esta forma volvemos las cosas mas faciles cuando solo se trata de mostrar informacion

class GeneralListApiView(generics.ListAPIView):
    serializer_class = None
    def get_queryset(self):
        #aca accedemos a el modelo de el serializador principal , aque que herede justo, esta clase en las general views en la carpeta Porducts , API, views general_views.py
        #ya que con esta instruccion obtenemos el Json de dicho modelo, sin tener que repetir codigo en las vistas generales
        model = self.get_serializer().Meta.model
        return model.objects.filter(state=True)