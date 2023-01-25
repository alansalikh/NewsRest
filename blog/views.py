from rest_framework.viewsets import ModelViewSet
from .models import Category, News, NewsImages
from .serializers import NewsSerializers, CategorySerializer, GetNewsSerializers, NewsImagesSerializers


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class NewsModelViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializers

    def get_serializer_class(self):
        if self.request.method in ('GET', 'HEAD', 'OPTIONS'):
            return GetNewsSerializers
        return NewsSerializers

class NewsImagesViewSet(ModelViewSet):
    queryset = NewsImages.objects.all()
    serializer_class = NewsImagesSerializers