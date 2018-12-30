from django.urls import path
from . import views
app_name="posts"
urlpatterns=[
path("add_post",views.add_post),
path("<slug:title>",views.post,name="post",),

]
