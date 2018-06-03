from urllib.parse import quote_plus
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect


from .forms import UserProfileForm
from .models import UserProfile


def profile_detail(request, username=None):
	instance = get_object_or_404(UserProfile, user=request.user)
	context = {
		"instance": instance,
	}
	return render(request, "user_detail.html", context)

def profile_create(request):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	form = UserProfileForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_abs_url())

	context = {
		"form": form
	}
	return render(request, "user_form.html", context)

def profile_list(request):
	querySet_list = UserProfile.objects.all()
	context = {
		"posts_list": querySet_list,
		"title": "O Squad",
	}
	return render(request, "user_list.html", context)

def profile_update(request, username=None):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	instance = get_object_or_404(UserProfile, user=request.user)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=false)
		instance.save()
		return HttpResponseRedirect(instance.get_abs_url())
		
	context = {
		"instance": instance,
		"form": form 
	}
	return render(request, "user_form.html", context)

def profile_delete(request, username=None):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	instance = get_object_or_404(UserProfile, user=request.user)
	instance.delete()

	return redirect("squad:list")
