from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from Post.serializer import PostSerializer
from .models import Post
from .forms import PostForm
from django.contrib import messages
from Post.models import Post

def all_posts(request):
    all_posts = Post.objects.all()

    context = {
        'all_posts' : all_posts,
    }

    return render (request, 'all_posts.html', context)



def post(request, id):
    #post = Post.objects.get(id=id)
    post = get_object_or_404 (Post, id=id)
    context = {
        'post' : post,
    }

    return render(request, 'detail.html', context)




def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            #new_form.user = request.user
            new_form.save()
            messages.success(request, 'Post Created Successfully')
            return redirect('/')

    else:
        form = PostForm()

    context = {
        'form' : form ,
    }

    return render(request, 'create.html', context)



def edit_post(request, id):
    post = get_object_or_404(Post , id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            new_form = form.save(commit=False)
            #new_form.user = request.user
            new_form.save()
            return redirect('/')


    else:
        form = PostForm(instance=post)

    context={
        'form' : form ,
    }

    return render(request, 'edit.html', context)

#def delete_post(request, id):
    #post = get_object_or_404(Post , id=id)
    #if request.method == 'POST':
        #form = PostForm(request.POST, instance=post)
        #if form.is_valid():
            #new_form = form.save(commit=False)
            #new_form.user = request.user
            #new_form.save()
            #return redirect('/')


    #else:
        #form = PostForm(instance=post)

    #context={
        #'form' : form ,
    #}

    #return render(request, 'delete.html', context)    






def delete_post(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully deleted post")
    return redirect("/")




class PostList(ListCreateAPIView):
    queryset  = Post.objects.all()
    serializer_class = PostSerializer


class PostViewSet(ModelViewSet):
    queryset  = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'Post_id'


class PostDelete(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'Post_id'