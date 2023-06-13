from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from .models import *
from django.views import View
from django.core.paginator import Paginator
from app.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator

# Create your views here.

#index page where User can only see blogs he/she can't make changes
def index(request):
    blog = Blog.objects.order_by('-date')
    return render(request,'index.html',{'blog':blog})

#registration of user
def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname= request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']

        #validation of user
        error_message = None 
        if not firstname:
            error_message = "firstname is required!!"

        elif not lastname:
            error_message = "lastname is required!!"

        elif not email:
            error_message = "email is required!!"
        elif not phone:
            error_message = "phone number is required"
        elif not password:
            error_message = "password is required"

        if error_message:
            return render(request,'register.html',{'error':error_message})
            
        user = Register(firstname=firstname,lastname=lastname,email=email,phone=phone,password=password)
        user.password = make_password(user.password)
        user.save()
        return redirect('blog')


    return render(request,'register.html')

#login functionality of user
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = Register.get_user_by_email(email)
        error_message = None 
        if user:
            flag = check_password(password,user.password)
            if flag:
                request.session['user'] = user.id # saving user id
                return redirect('blog')
            else:
                error_message = "email or password not valid!!"
        return render(request,'login.html',{'error':error_message})
    return render(request,'login.html')

#logout functionality
def logout(request):
    request.session.clear()
    return redirect('/')

#class based views with middleware 
class blog_uploading_section(View):
    def post(self,request):
        title = request.POST['title']
        text = request.POST['text']

        user = Blog(title=title,text=text)
        user.save()
        return redirect('blog')
    
    @method_decorator(auth_middleware)
    def get(self,request):
        return render(request,'home.html')

# blog writing portion
def home(request):
    return render(request,'home.html')

#blog display section with pagination
class blog(View):
    
    @method_decorator(auth_middleware)
    def get(self,request):
        user_blog = Blog.objects.all()
        # print(user_blog)
        paginator = Paginator(user_blog,8)#pagination limit
        # print(paginator)
        page_number = request.GET.get("page")
        # print(page_number)
        page_obj = paginator.get_page(page_number)
        # print(page_obj)
        context={
                'page_obj':page_obj
        }
        return render(request,'blog.html',context)

#blog update functionality
def update(request,id):
    mem = Blog.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})

#update record functionality
def uprec(request,id):
    if request.method == 'POST':
        title = request.POST['title']
        discription = request.POST['discription']
        text = request.POST['text']

        mem = Blog.objects.get(id=id)
        mem.title = title
        mem.discription = discription
        mem.text = text
        mem.save()
    return redirect('blog')

#delete blog 
def delete_blog(request,id):
   d =  Blog.objects.get(id=id)
   d.delete()
   return redirect('blog')



    
