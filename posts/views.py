from urllib.parse import quote_plus
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.functional import SimpleLazyObject
import re



from .forms import PostForm
from .models import Post


def post_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	if instance.draft:
		if not (request.user.is_staff or request.user.is_superuser):
			raise Http404

	shareStr = quote_plus(instance.content) 
	tag_data = create_tag_data(instance)
	context = {
		"title": instance.title,
		"instance": instance,
		"shareStr": shareStr,
		"tags": tag_data
	}
	return render(request, "post_detail.html", context)

def post_create(request):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404

	if not request.user.is_authenticated:
		raise Http404

	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		#instance.user.user = request.user
		instance.save()
		return HttpResponseRedirect(instance.get_abs_url())

	context = {
		"form": form 
	}

	return render(request, "post_form.html", context)

def post_list(request):
	if not (request.user.is_staff or request.user.is_superuser):
		querySet_list = Post.objects.active()
	else:
		querySet_list = Post.objects.all()
	
	query = request.GET.get("q")
	if query:
		querySet_list = Post.objects.filter(
			Q(title__icontains=query) |
			Q(content__icontains=query) |
			Q(tags__icontains=query)
		).distinct()

	paginator = Paginator(querySet_list, 5) # Show 5 querySets per page
	page_request_var = 'pagina'
	page = request.GET.get(page_request_var)
	try:
		querySet = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		querySet = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		querySet = paginator.page(paginator.num_pages)


	context = {
		"posts_list": querySet,
		"title": "Blog",
		"page_request_var": page_request_var,
	}

	return render(request, "post_list.html", context)


def post_update(request, slug=None, id=None):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	instance = get_object_or_404(Post, slug=slug, id=id)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=false)
		instance.save()
		return HttpResponseRedirect(instance.get_abs_url())
		
	context = {
		"title": instance.title,
		"instance": instance,
		"form": form 
	}

	return render(request, "post_form.html", context)

def post_delete(request, slug=None):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()

	return redirect("blog:list")

def create_tag_data(post):
    tag_data = []
    count = {}
    tags = re.split(",", post.tags)
    for tag in tags:
        tag_data.append(tag)
    return tag_data

