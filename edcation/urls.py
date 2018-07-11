

from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path("about",views.about,name="about"),
    path("faq",views.faq,name="faq"),
    path("post",include("posts.urls",namespace="posts")),
]
