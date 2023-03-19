from django.db.models import Count
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import *


class ListAllUsers(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserSortByPosts(ListAPIView):
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = User.objects.annotate(num_posts=Count('posts')).order_by('-num_posts')
        serializer = UserSortByPostsSerializer(queryset, many=True)

        return Response(serializer.data)
