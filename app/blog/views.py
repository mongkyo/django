import re

from django.http import HttpResponse
from django.shortcuts import render

from .models import Post


def post_list(request):
    posts = Post.objects.order_by('-created_date')
    context = {
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post': post,
    }
    # templates/blog/post_detail.html
    #  post가 가진 title, text, author, created_date, published_date를 적절히 출력
    # request.path에 있는 문자열을
    #   /posts/12345/
    #   /posts/3/
    # 위의 경우 정규표현식으로 적절히
    # 12345와 3문자열을 추출
    # 추출한 결과를 HttpResponse에 리턴
    # m = re.search(r'^/posts/(?P<pk>\d+)/$', request.path)
    # pk = m.group('pk')
    return render(request, 'blog/post_detail.html', context)
