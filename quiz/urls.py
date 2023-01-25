from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('quiz', QuizModelViewSet)
router.register('question', QuestionModelViewSet)
router.register('answer', AnswerModelViewSet)

urlpatterns = router.urls