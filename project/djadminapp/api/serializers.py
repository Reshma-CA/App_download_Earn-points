from rest_framework import serializers
from userapp.models import Category, SubCategory, App,People,UserProfile,Task

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category']
        
class AppSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(read_only=True)
    # sub_category = SubCategorySerializer(read_only=True)
    # app_image = serializers.SerializerMethodField()  # Add this line

    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    sub_category = serializers.PrimaryKeyRelatedField(queryset=SubCategory.objects.all())
    
    # Make app_image writable so it can accept file uploads
    app_image = serializers.ImageField(required=True)


    class Meta:
        model = App
        fields = ['id', 'name', 'app_link', 'points', 'category', 'sub_category', 'app_image']

    def get_app_image(self, obj):
        request = self.context.get('request')
        if obj.app_image:
            return request.build_absolute_uri(obj.app_image.url)
        return None
