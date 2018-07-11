from django.shortcuts import render

def post(request,title):
    return render(request,"posts/post.html")
