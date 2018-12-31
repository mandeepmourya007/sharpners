from django.db import models



class posts(models.Model):
    title = models.CharField(max_length=200,blank=True,null=True)
<<<<<<< HEAD
    tag=models.CharField(max_length=100,blank=True,null=True)
   # slug=models.SlugField(unique=True)

=======
    slug=models.SlugField(unique=True)
>>>>>>> c7acea81d494c5462857d49108e43b53e7412ac7
    text = models.TextField(blank=True,null=True)
    image=models.FileField(upload_to="static/images/post",blank=True,null=True)
    def __str__(self):
    	return self.title