from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect

from rest_framework import viewsets, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import MessageSerializer, UserSerializer
from .models import Message, deserialize_user


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


def message_list(request):
    return redirect('message-list-page', page=0)


class MessageList(APIView):
    """Create/Get Chat messages."""

    def get(self, request, *args, **kwargs):
        """
        List all messages, 10 per page, or create a new message.
        """
        if kwargs:
            page = kwargs['page']
            if page == "":
                page = 0
            else:
                page = int(page)

            if page < 0:
                return Response({
                    {"status_code": 404, "detail": "This page doesn't exists'."}
                })
            elif page > Message.objects.count():
                messages = Message.objects.all()[-10:]
            else:
                messages = Message.objects.all()[page*10:(page+1)*10]
        else:
            messages = Message.objects.all()[:10]

        return Response({
            'messages': MessageSerializer(messages, many=True, context={'request': request}).data
        })


class MessageDetail(APIView):
    """
    Create/Get Chat messages
    """
    def get(self, request, *args, **kwargs):
        """
        List all messages, 10 per page, or create a new message.
        """
        if kwargs:
            message_id = int(kwargs['pk'])
            # message_id = int(message_id)
            message = Message.objects.get(id=message_id)
        else:
            message = Message.objects.all().first()

        return Response({
            'messages': MessageSerializer(message, many=False, context={'request': request}).data
        })


class MessageCreate(APIView):
    def post(self, request, *args, **kwargs):
        """
        Сreate a new message
        """
        message = self.request.data['message']

        user = self.request.user

        return Response({
            'status': 'SUCCESS', 'message': message, 'user': deserialize_user(user)
        })
