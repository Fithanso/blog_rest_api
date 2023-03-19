from rest_framework.serializers import ModelSerializer

from .models import *


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class MarkedPostSerializer(ModelSerializer):
    class Meta:
        model = MarkedPost
        fields = '__all__'
