from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def blog_posts(request):
    blogs = Blog.objects.all()  # gets all of the blog posts from the database and store them in a variable
  
    # creates the context dictionary to send the blog posts to the template
    context = {
       'blogs': blogs
    }
    return render(request, 'pages/posts.html', context)

def add_post(request):
    if request.method == 'GET': # if its a GET request, just display the add.html template
        return render(request, 'pages/add.html')
    elif request.method == 'POST': # if it's a POST request ..
        title = request.POST['title']   # get the title from the POST submission, this comes from a form
        text = request.POST['text']     # get the text from the POST submission, this comes from a form
        pub_date = request.POST['pub_date']
        # add the new blog post to the database. objects.create() automatically saves the new blog post for us.
        Blog.objects.create(title = title, text = text, pub_date = pub_date)
        return redirect('posts')
   
def delete_post(request, id):
    blog_post = Blog.objects.get(id=id)
    print(blog_post) ## check the terminal, it should output the object before it gets deleted
    blog_post.delete()
    return redirect('posts')   

def see_details(request, id): ##we get the id of the element. Remember, all elements are created with an ID in the database.
    post = Blog.objects.get(id = id) ## we are assigning the element to a variable
    return render(request, 'pages/details.html', {"post": post}) ## we are passing the context to the page

def update_post(request, id):
    blog_post = Blog.objects.get(id=id)
    blog_post.title = request.POST['title']
    blog_post.text = request.POST['text']
    blog_post.pub_date = request.POST['pub_date']
    print(blog_post)
    blog_post.save()
    return redirect('posts')

def delete_post(request, id):
    blog_post = Blog.objects.get(id=id)
    print(blog_post) ## check the terminal, it should output the object before it gets deleted
    blog_post.delete()
    return redirect('posts')


# Create your views here.
