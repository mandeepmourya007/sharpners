from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . forms import postForm
from .models import posts

def post(request,title):
<<<<<<< HEAD
	post=posts.objects.all()
	return render(request,"posts/post.html",{ "title":title, "post":post } )
def add_post(request):
	
	if request.method=="POST":
		title=request.POST.get("title")
		print(title)
		tag=request.POST.get("tag")
		text=request.POST.get("text")
		# print(title,tag,text)
		#use forms?????????
		#form=postForm(tag,title,text)
		o=posts(title=title,tag=tag,text=text)
		print("gat ",o," detaui")
		
		if (title and tag and text):
			o.save()
			return HttpResponse('Thank you post added')
		else:
			return HttpResponse('Please enter all field')

		

=======
    return render(request,"posts/post.html",{"title":title})
def add_post(request):
>>>>>>> c7acea81d494c5462857d49108e43b53e7412ac7
	return render(request,"posts/add_post.html")