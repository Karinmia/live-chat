from django.urls import include, path

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
# router.register('messages', views.MessageViewSet)
router.register('users', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('messages/', views.message_list, name='message_list'),
    path('messages/<int>/', views.MessageList.as_view(), name='message-list-page'),
    path('messages/id/<uuid:pk>/', views.MessageDetail.as_view(), name='message-detail'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]