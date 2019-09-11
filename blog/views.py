from django.shortcuts import render
from blog.models import BlogPost


def post_list(request):
    return render(
        request, "blog/post_list.html", {"posts": BlogPost.objects.published()}
    )
