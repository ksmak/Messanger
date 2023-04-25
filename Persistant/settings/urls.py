from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from messagess.views import (
    MessageViewSet,
    ChatViewSet
)

router = DefaultRouter(
    trailing_slash=False
)

router.register('chats', ChatViewSet, basename='chat')
router.register('messages', MessageViewSet, basename='message')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
