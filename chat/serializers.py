from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Message


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


# Serializers define the API representation.
class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'text', 'created_at')

    # def create(self, validated_data):
    #     Message.objects.create(author=self.user, **validated_data)
    #     return message
