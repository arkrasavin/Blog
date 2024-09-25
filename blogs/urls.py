from django.urls import path

from blogs import views


app_name = 'blogs'

urlpatterns = [
    path('', views.index, name='index'),
    path('all_blogs/', views.all_blogs, name='all_blogs'),
    path('blog/<int:blog_id>/', views.blog, name='blog'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('new_post/<int:blog_id>/', views.new_post, name='new_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]
