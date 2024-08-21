from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Category, SubCategory, App,People,UserProfile,Task
from .serializers import AppSerializer

class AppListAPIView(APIView):
    def get(self, request):
        apps = App.objects.all()
        serializer = AppSerializer(apps, many=True, context={'request': request})  # Pass the request context
        return Response(serializer.data)

# class UserDetails(APIView):
#     def get(self, request, *args, **kwargs):
#         id = kwargs.get('id')  # Assuming the id is passed in the URL
#         obj = UserProfile.objects.get(id=id)
#         serializer = UserProfileSerializer(obj)
#         return Response(serializer.data)