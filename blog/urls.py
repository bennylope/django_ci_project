from django.urls import include
from django.urls import path
from blog.views import post_list

urlpatterns = [path("", view=post_list, name="post_list")]
