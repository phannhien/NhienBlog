from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
# Create your views here.
def list(request):
    Data = {'Posts': Post.objects.all().order_by("date")}
    return render(request, 'blog/blog.html', Data)