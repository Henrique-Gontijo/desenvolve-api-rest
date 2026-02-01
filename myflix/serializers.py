from rest_framework import serializers
from myflix.models import User, Stream, List

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'cpf', 'birth_date', 'cell_phone']

class StreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stream
        fields = '__all__'

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        exclude = []

class ListUserSerializer(serializers.ModelSerializer):
    stream = serializers.ReadOnlyField(source='stream.description')

    class Meta:
        model = List
        fields = ['stream']

    def get_category(self, obj):
        return obj.get_category_display()

class ListStreamSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.name')

    class Meta:
        model = List
        fields = ['user_name']