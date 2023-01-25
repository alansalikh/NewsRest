from rest_framework.routers import DefaultRouter
from .views import CategoryModelViewSet, NewsModelViewSet, NewsImagesViewSet


router = DefaultRouter()

router.register('category', CategoryModelViewSet)
router.register('news', NewsModelViewSet)
router.register('news_images', NewsImagesViewSet)

urlpatterns = router.urls