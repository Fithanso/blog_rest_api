from rest_framework.authtoken.admin import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'last_login']


class UserSortByPostsSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.CharField(max_length=254)
    last_login = serializers.DateTimeField()
    num_posts = serializers.CharField(max_length=5)
