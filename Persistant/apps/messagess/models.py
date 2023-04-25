from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser

User: AbstractBaseUser = get_user_model()

class Chat(models.Model):
    """
    Chat. Can be 1 people
    """
    owner: User = models.ForeignKey(
        to=User,
        related_name="own_chats",
        on_delete=models.CASCADE,
        verbose_name="создатель",
        null=True,
        blank=True
    )
    is_many: bool = models.BooleanField(
        verbose_name="групповой ли чат",
        default=False
    )
    name: str = models.CharField(
        verbose_name="название",
        max_length=120
    )
    members: list[User] = models.ManyToManyField(
        to=User,
        related_name='chats'
    )

    class Meta:
        ordering = ('-id', )
        verbose_name = 'чат'
        verbose_name_plural = 'чаты'

    def __str__(self) -> str:
        return (
            f"Owner: {self.owner if self.owner is not None else 'Basic'}. "
            f"Count users {len(self.members.get_queryset())}"
        )

class Message(models.Model):
    """
    Message between
    """
    sender: 'User' = models.ForeignKey(
        to=User,
        related_name='messages',
        on_delete=models.CASCADE
    )
    to_send = models.ForeignKey(
        to=Chat,
        related_name='messages',
        verbose_name="чат",
        on_delete=models.CASCADE
    )
    text = models.TextField(
        verbose_name="сообщение",
        max_length=200
    )
    datetime_send = models.DateTimeField(
        verbose_name="время отправления",
        auto_now=False,
        auto_now_add=True
    )

    class Meta:
        ordering = ('-datetime_send', )
    
    def __str__(self) -> str:
        return f"[{self.datetime_send.strftime('%d %B - %H:%M:%S')}] {self.text}"
