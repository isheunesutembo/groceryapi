from rest_framework.decorators import  api_view
from rest_framework.response import Response
from .serializers import ProductCategorySerializer,ProductSerializer
from .models import Product,ProductCategory

@api_view(['GET'])
def getproductcategories(request):
    categories=ProductCategory.objects.all()
    serializer=ProductCategorySerializer(categories,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getproductcategory(request,pk):
    category=ProductCategory.objects.get(id=pk)
    serializer=ProductCategorySerializer(category,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createproductcategory(request):
    data=request.data
    category=ProductCategory.objects.create(body=data['body'])
    serializer=ProductCategorySerializer(category,many=False)
    return Response(serializer.data)




