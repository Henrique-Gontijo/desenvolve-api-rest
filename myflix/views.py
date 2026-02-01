from rest_framework import viewsets, generics
from myflix.models import User, Stream, List
from myflix.serializers import (UserSerializer, StreamSerializer, ListSerializer,
    ListUserSerializer, ListStreamSerializer)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StreamViewSet(viewsets.ModelViewSet):
    queryset = Stream.objects.all()
    serializer_class = StreamSerializer

class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer

class ListUser(generics.ListAPIView):
    def get_queryset(self):
        queryset = List.objects.filter(user_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListUserSerializer

class ListStream(generics.ListAPIView):
    def get_queryset(self):
        queryset = List.objects.filter(stream_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListStreamSerializer