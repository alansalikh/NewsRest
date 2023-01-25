from rest_framework import serializers
from .models import Category, News, NewsImages

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'slug')

class NewsImagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = NewsImages
        fields = ('id', 'news', 'image')

class GetNewsImagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = NewsImages
        fields = ('image',)

class GetNewsSerializers(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    news_images = GetNewsImagesSerializers(many=True ,read_only=True)
    class Meta:
        model = News
        fields = ('id', 'title', 'category', 'image', 'text', 'created_at', 'news_images')

class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'category', 'image', 'text', 'created_at')

