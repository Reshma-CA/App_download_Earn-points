
from rest_framework.views import APIView
from rest_framework.response import Response
from userapp.models import Category, SubCategory, App,People,UserProfile,Task
from .serializers import AppSerializer,CategorySerializer,SubCategorySerializer
from rest_framework import status
    
class CategoryListAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class SubCategoryListAPIView(APIView):
    def get(self, request):
        category_id = request.query_params.get('category_id')
        if category_id:
            subcategories = SubCategory.objects.filter(category_id=category_id)
        else:
            subcategories = SubCategory.objects.all()
        serializer = SubCategorySerializer(subcategories, many=True)
        return Response(serializer.data)
    
class AdminAppCreationAPIView(APIView):
    def get(self, request):
        apps = App.objects.all()
        serializer = AppSerializer(apps, many=True, context={'request': request})  # Pass the request context
        return Response(serializer.data)
    
    def post(self,request):
        data = request.data
        serializer= AppSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
