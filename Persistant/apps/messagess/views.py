from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .models import Chat, Message
from .serializers import (
    MessageSerializer,
    CreateMessageSerializer,
    ChatSerializer,
    CreateChatSerializer
)


class MessageViewSet(ViewSet):
    """Message viewset."""

    def list(self, request):
        queryset = Message.objects.all()
        serializer = MessageSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = Message.objects.get(pk=pk)
        serializer = MessageSerializer(
            instance=queryset
        )
        return Response(serializer.data)

    def create(self, request):
        serializer = CreateMessageSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)
        
        return Response(serializer.data)

    def update(self, request, pk):
        queryset = Message.objects.get(pk=pk)

        serializer = CreateMessageSerializer(
            instance=request.data,
            data=request.data
        )

        serializer.is_valid(raise_exception=True)
        
        return Response(serializer.data)


class ChatViewSet(ViewSet):
    """Chat viewset."""

    def list(self, request):
        queryset = Chat.objects.all()
        serializer = ChatSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = Chat.objects.get(pk=pk)
        serializer = ChatSerializer(
            instance=queryset
        )
        return Response(serializer.data)

    def create(self, request):
        serializer = CreateChatSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)
        
        return Response(serializer.data)

    def update(self, request, pk):
        queryset = Chat.objects.get(pk=pk)

        serializer = CreateChatSerializer(
            instance=request.data,
            data=request.data
        )

        serializer.is_valid(raise_exception=True)
        
        return Response(serializer.data)
