from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import CreateView,DeleteView,UpdateView,ListView,DetailView,TemplateView
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy
from bloging.models import Post,Comment
from bloging.forms import PostForm,CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class About(TemplateView):
    template_name='about.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='About us'
        return context


class PostListView(ListView):
    model=Post
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    
class PostDetailView(DetailView):
    model=Post

class PostCreateView(LoginRequiredMixin,CreateView):
    login_url='/login/'
    redirect_field_name='bloging/post_detail.html'
    form_class=PostForm
    model=Post

    
class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url='/login/'
    redirect_field_name='bloging/post_detail.html'
    form_class=PostForm
    model=Post


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model=Post
    success_url=reverse_lazy('list')

class PostDraftView(LoginRequiredMixin,ListView):
    login_url='/login/'
    redirect_field_name='bloging/post_list.html'
    model=Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')



@login_required
def PostComment(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=CommentForm()
    return render(request,'bloging/comment_form.html',{'form':form})



@login_required
def AproveComment(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)
    
@login_required
def CommentRemove(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)

@login_required
def PostPublish(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=post.pk)
    