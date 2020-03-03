from apps.forumkg.models import Post
from django.views.generic import ListView, DetailView

#function based view
# def index(request):
#     return render(request, 'forum/index.html',  {})


class IndexPageView(ListView):
    template_name = 'forum/index.html'
    model = Post


class PostDetailView(DetailView):
    template_name = 'forum/post_detail.html'
    model = Post
