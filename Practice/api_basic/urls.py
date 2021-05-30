
from django.urls import path, include
# from .views import article_list, article_detail
from .views import ArticleAPIView, ArticleSingle, GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>', include(router.urls)),
    # path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    path('article/<int:id>', ArticleSingle.as_view()),
    path('generic/article/<int:id>', GenericAPIView.as_view()),
]