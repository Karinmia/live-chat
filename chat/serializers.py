from django.contrib.auth.models import User

from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from .models import Message, deserialize_user


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


# Serializers define the API representation.
class MessageSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'text', 'author', 'created_at', 'updated_at')
        read_only_fields = ('author',)

    def perform_create(self, serializer):
        serializer.save(author=deserialize_user(self.request.user))
