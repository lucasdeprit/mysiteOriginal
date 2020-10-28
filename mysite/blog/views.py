# Create your views here.
from django.shortcuts import render
from django.views import generic

from . import forms
from .forms import Myform
from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def loginform(request):
    form = Myform()
    return render(request, 'blog/login.html', {'form': form})


class Myform(forms.Form):
    nombre = forms.CharField(label='introduce tu nombre', max_length=100)
    email = forms.CharField(label='introduce tu nombre', max_length=20)
