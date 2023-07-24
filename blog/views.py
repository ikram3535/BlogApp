from django.shortcuts import render , get_object_or_404,HttpResponseRedirect,redirect
from blog.models import Post , Category , Comments
from django.core.paginator import Paginator , EmptyPage ,PageNotAnInteger
from django.db.models import Q
from blog.forms import CommentForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render

def Explore(request):
    return render(request, "explore.html")

def Creaters(request):
    return render(request,"creaters.html")
def Archive(request):
    return render (request,"archive.html")
def category(request):
    return render (request,"category_show.html")


def send(request):
    return render(request, "index.html")

def contact_us(request):
    return render(request, 'ContactUs.html')


def index(request):
    context = dict()
    post_list= Post.objects.all()
    query = request.GET.get("q")

    if query:
        post_list = post_list.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        ).distinct()
    paginator = Paginator(post_list , 3)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context["posts"] = posts
    context["post_list"] = Post.objects.distinct()
    context["cat"] = Category.objects.all()
    # pagination , search
    return render (request , "index.html" , context)
    

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url())
    context= {
        "post": post,
        "form": form,
    }
    
    return render(request, "detail.html", context)

def add_comment_to_post(request,pk):
    post = Post.get_object_or_404(Post, pk)

    if request.POST == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("detail",pk=post.pk)
    else:
        form = CommentForm()

    return render(request,"forms.html", {"form": form})

@login_required
def comment_approved(request,pk):
    comment = get_object_or_404(Comments, pk=pk)
    comment.approve()
    return redirect("detail", pk = comment.post.pk)


@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comments,pk=pk)
    comment.delete()
    return redirect("detail",pk=comment.post.pk)




def category_show(request,category_slug):
    context = dict()
    context["category"] = get_object_or_404(
        Category, slug=category_slug,
    )

    context["items"] = Post.objects.filter(
        category = context["category"]
    )





    return render(request,"category_show.html",context)