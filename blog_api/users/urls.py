
from django.urls import path, re_path, include

from .views import *


app_name = 'users'

urlpatterns = [
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('all/', ListAllUsers.as_view(), name='list-all'),
    path('sorted-by-posts/', UserSortByPosts.as_view(), name='sorted-by-posts')
]
