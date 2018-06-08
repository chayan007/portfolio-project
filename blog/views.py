from django.shortcuts import render,get_object_or_404
from .models import blog

def allblog(request):
    blogs=blog.objects
    return render(request, 'blog/allblogs.html',{'blogs':blogs})
    pass

def detail(request,blog_id):
    details=get_object_or_404(blog, pk=blog_id)
    return render(request,'blog/detail.html',{'blog':details})
    pass