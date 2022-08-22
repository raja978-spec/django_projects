from django.db import IntegrityError, connection
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as Login
from django.contrib.auth import logout as Logout
from datetime import date, datetime
from bs4 import BeautifulSoup
from NewBlogApp.models import user_created_blog
global name 

def fullviewpost(request,id):
    full_blog=user_created_blog.objects.get(id=id)
    return render(request,'fullviewpost.html',{'full_blog':full_blog})
     
@login_required
def editblog(request,id):
    global name 
    edit_blog=user_created_blog.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get('username')
        Title=request.POST.get('title')
        Subtitle=request.POST.get('subtitle')
        content=request.POST.get('editor')
        Date=datetime.today()
        '''
        with open(f'blogapp/User_Creation_Blogs/{Title}.html',"w") as f:
            f.write(content)
        '''
        c=connection.cursor()
        c.execute(f'update NewBlogApp_user_created_blog set user="{name}",date="{Date}",title="{Title}",subtitle="{Subtitle}",content="{content}" WHERE id="{id}"')
        return redirect('home')
    return render(request,'create_blog.html',{'edit_blog':edit_blog})
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def blogpost(request):
    saved_blogs=user_created_blog.objects.all()
    return render(request,'Blog_post.html',{'user_created_blogs':saved_blogs})
     
def page404(request):
    return render(request,'404.html')

def home(request):  
    data=user_created_blog.objects.filter(user=name)
    return render(request,'home.html',{'user_created_blogs':data})

def login(request):
    global name 
    if request.method=="POST":
        username=request.POST["username"]
        pass1=request.POST["password"]
        user=authenticate(username=username,password=pass1)
        
        if user is not None:
            Login(request,user)
            name=username  
            return redirect('home')
        else:
            message='Please enter valid details'
            return render(request,'login.html',{'message':message})

    return render(request,'login.html')

def logout(request):
    Logout(request)
    return redirect('blogpost')
    
def register(request):
    if request.method=="POST":
       
        username=request.POST.get("username")
        fname=request.POST.get("first_name")
        lname=request.POST.get("last_name")
        email=request.POST.get("email")
        pass1=request.POST.get("password")
        pass2=request.POST.get("password_repeat")
        
        if pass1==pass2:
            try:
              myusers=User.objects.create_user(username,email,pass1)
              myusers.last_name=lname
              myusers.first_name=fname
              myusers.save()
            except IntegrityError as e:
                message='''
                Your have already registered...
                Please try to login 
                ''' 
                return render(request,'register.html',{'message':message})
            return redirect('login')
        else:
            message="Please check if you entered details is correct"
            return render(request,'register.html',{'message':message})
    return render(request,'register.html')
    
def forget_pasword(request):
    return render(request,'forgot-password.html')
def profile(request):
    return render(request,'profile.html')

@login_required
def create_blog(request,name=None):
    '''
    if name != None:
        file=" ".join(open(f'blogapp/User_Creation_Blogs/{name}.html','r').readlines())
        t=name
        return render(request,'create_blog.html',{'file':file,'title':t})
    '''
    if request.method=='POST':
        Title=request.POST['title']
        Subtitle=request.POST['subtitle']
        content=request.POST['editor']
        UserName=request.POST.get('username')
         
        '''
        with open(f'blogapp/User_Creation_Blogs/{Title}.html',"w") as f:
            f.write(content)
        '''
        blog_object=user_created_blog()
        blog_object.date=datetime.today()
        blog_object.user=UserName
        blog_object.title=Title
        blog_object.subtitle=Subtitle
        blog_object.content=content
        blog_object.save()
        return redirect('home')
    return render(request,'create_blog.html')

def delete(request,id):
    blog_object=user_created_blog.objects.get(id=id)
    blog_object.delete()
    return redirect('home')
def required(request):
    if request.method=="POST":
        username=request.POST["username"]
        pass1=request.POST["password"]
        user=authenticate(username=username,password=pass1)
        
        if user is not None:
            Login(request,user)
            return redirect('home')
        else:
            message='Please enter valid details'
            return render(request,'login.html',{'message':message})
    return render(request,'login.html',{'message':"You have to login to go home"})











