from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from backend.models import Product, Category, CategoryClient
from backend.serializers import ProductSerializer, CategorySerializer, CategoryClientSerializer



#Productos

@api_view(['POST'])
@permission_classes([AllowAny])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([AllowAny])
def list_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_product(request, id):
    product = Product.objects.get(id=id)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return Response(status=204)

#Categoria

@api_view(['POST'])
@permission_classes([AllowAny])
def create_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([AllowAny])
def list_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_category(request, id):
    category = Category.objects.get(id=id)
    serializer = CategorySerializer(instance=category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_category(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return Response(status=204)

#Categoria Cliente

@api_view(['POST'])
@permission_classes([AllowAny])
def create_categoryclient(request):
    serializer = CategoryClientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([AllowAny])
def list_categoriesclient(request):
    categories = CategoryClient.objects.all()
    serializer = CategoryClientSerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_categoryclient(request, id):
    category = CategoryClient.objects.get(id=id)
    serializer = CategoryClientSerializer(instance=category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_categoryclient(request, id):
    category = CategoryClient.objects.get(id=id)
    category.delete()
    return Response(status=204)


