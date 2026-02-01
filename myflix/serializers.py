from rest_framework import serializers
from myflix.models import User, Stream

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'cpf', 'birth_date', 'cell_phone']

class StreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stream
        fiels = '__all__'