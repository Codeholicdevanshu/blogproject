
from django.urls import path,include
from app import views
from .views import blog, blog_uploading_section, register

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('home',views.home,name='home'),
    path('blog_upload',blog_uploading_section.as_view(),name="blog_upload"),
    path('blog',blog.as_view(),name='blog'),
    path('delete/<int:id>',views.delete_blog,name='delete_blog'),
    path('logout',views.logout,name='logout'),
    path('update/<int:id>/',views.update,name='update'),
    path('update/uprec/<int:id>/',views.uprec,name="uprec")
]