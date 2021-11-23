from django.urls import path
from . import views

app_name = "posts"

urlpatterns=[
  path('index/',views.index,name="index"),
  path('post_detail/<int:post_id>', views.post_detail,name="post_detail")
]