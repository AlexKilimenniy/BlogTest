from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from blog.models import *
from django.views import generic as cbv


class PostsListView(cbv.TemplateView):
    template_name = 'posts_list.html'
    model = PostMessage
    paginate_by = 25

    def get_context_data(self, **kwargs):
        posts = PostMessage.objects.all()
        comments = Comment.objects.all()
        try:
            context = super(PostsListView, self).get_context_data(**kwargs)
            context['post_massages'] = posts
            context['comments'] = comments
            return context
        except Http404:
            self.kwargs['page'] = 1
            context = super(PostsListView, self).get_context_data(**kwargs)
            context['post_massages'] = posts
            context['comments'] = comments
            return context


def addlike(request, pk):
    post = get_object_or_404(PostMessage, pk=pk)
    post.likes += 1
    post.save()
    return HttpResponseRedirect('/blog/')
