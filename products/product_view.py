from rest_framework import generics
from base.general import GeneralListApiView
from rest_framework import viewsets
from .product_serializer import ProductoSerializer
from rest_framework import status
from rest_framework.response import Response
from users.authmixin import Authentication


class ProductoViewSet(Authentication,viewsets.ModelViewSet):
    
    serializer_class = ProductoSerializer
    
    def get_queryset(self, pk=None):
        
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()
    
    def list(self, request):
        product_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response (product_serializer.data, status = status.HTTP_200_OK)
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Producto creado correctamente'}, status = status.HTTP_201_CREATED)
        return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response (product_serializer.data, status = status.HTTP_200_OK)
            return Response (product_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        product = self.get_queryset().filter(id = pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message': 'Producto eliminado correctamente'}, status = status.HTTP_200_OK)
        return Response({'message': 'Producto no encontrado con esos datos'}, status = status.HTTP_400_BAD_REQUEST)

    
""" class ProductoListCreateAPIVew(generics.ListCreateAPIView):
    serializer_class = ProductoSerializer
    queryset = ProductoSerializer.Meta.model.objects.filter(state = True)
    
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Producto creado correctamente'}, status = status.HTTP_201_CREATED)
        return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)



class ProductoRetrieveUpdateDestroyAPIVew(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductoSerializer
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()
            
       
    
    def patch(self, request, pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk))
            return Response (product_serializer.data, status = status.HTTP_200_OK)
        return Response({'message': 'Producto no encontrado con esos datos'}, status = status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response (product_serializer.data, status = status.HTTP_200_OK)
            return Response (product_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        product = self.get_queryset().filter(id = pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message': 'Producto eliminado correctamente'}, status = status.HTTP_200_OK)
        return Response({'message': 'Producto no encontrado con esos datos'}, status = status.HTTP_400_BAD_REQUEST) """





    
    

    