from django.urls import path
from apps.forumkg.views import IndexPageView, PostDetailView

urlpatterns = [
    #index page url
    path('', IndexPageView.as_view(), name='index'),
    path('post/<str:slug>/', PostDetailView.as_view(), name='post_detail'),
]

