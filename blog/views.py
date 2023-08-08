from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth import login
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Post
from .forms import CommentForm


class FavouriteList(generic.ListView):

    def favourite_list(request):
        new = Post.newmanager.filter(favourites=request.user)
        return render(request, 'favourites.html',
        {'new': new})

class Favourite(generic.ListView):
    
    def favorite_add(request, id):
        post = get_object_or_404(Post, id=id)
        if post.favourites.filter(id=request.user.id).exists():
            post.favourites.remove(request.user)
        else:
            post.favourites.add(request.user)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


class PostList(generic.ListView):
    """
    A view to display a list of published blog post
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/blog.html'
    paginate_by = 6


class PostDetail(View):
    """
    A view to display a single blog post and check if the user has liked it 
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'blog/post_detail.html',
            {
                'post': post,
                'liked': liked
            },
        )


class PostLike(View):
    """
    A view to handle liking or unliking a blog post
    """

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            messages.success(request, 'Blog unliked!')
        else:
            post.likes.add(request.user)
            messages.success(request, 'Blog liked!')

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
