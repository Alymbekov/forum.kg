from django.urls import path
from apps.forumkg.views import index

urlpatterns = [
    #index page url
    path('', index, name='index'),
]

