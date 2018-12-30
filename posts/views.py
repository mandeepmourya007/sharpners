from django.shortcuts import render

def post(request,title):
    return render(request,"posts/post.html",{"title":title})
def add_post(request):
	return render(request,"posts/add_post.html")