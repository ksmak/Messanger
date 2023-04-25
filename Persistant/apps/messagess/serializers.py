from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Chat, Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            'password',
            'is_staff',
            'is_superuser',
            'last_login',
            'date_joined',
            'groups',
            'user_permissions'
        )


class ChatSerializer(serializers.ModelSerializer):
    """Chat serializer."""
    owner = UserSerializer()
    members = UserSerializer(many=True)

    class Meta:
        model = Chat
        fields = (
            'owner',
            'is_many',
            'name',
            'members'
        )


class CreateChatSerializer(serializers.ModelSerializer):
    """Chat serializer."""
    class Meta:
        model = Chat
        fields = (
            'owner',
            'is_many',
            'name',
            'members'
        )

    def validate(self, data):
        if not data['is_many']:
            if len(data['members']) != 2:
                raise serializers.ValidationError(
                    "Кол-во участников должно быть равно 2"
                )

        return data


class MessageSerializer(serializers.ModelSerializer):
    """Message serializer."""
    sender = UserSerializer()

    class Meta:
        model = Message
        fields = (
            'sender',
            'to_send',
            'text',
            'datetime_send'
        )


class CreateMessageSerializer(serializers.ModelSerializer):
    """Message serializer."""
    class Meta:
        model = Message
        fields = (
            'sender',
            'to_send',
            'text',
            'datetime_send'
        )
