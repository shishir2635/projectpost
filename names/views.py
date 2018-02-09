from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import names,posts
from .forms import nameform,postform
from django.core.paginator import Paginator


def Index(request):
	nameofstudents = names.objects.all().order_by('-num_posts')
	return render(request,'names/index.html',{'names':nameofstudents,})

def person_detail(request,pk):
	student = names.objects.get(pk=pk)
	post_list = posts.objects.filter(name=student)
	paginator = Paginator(post_list,7)
	page = request.GET.get('page')
	posts_all = paginator.get_page(page)
	return render(request,'names/person_detail.html',{'student':student,'posts':posts_all,})

def add_name(request):
	if request.method == 'POST':
		form = nameform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('Index')
	else:
		form = nameform()

	return render(request,'names/add_person.html',{'form':form,})

def add_post(request,pk):
	if request.method == "POST":
		form = postform(request.POST)
		if form.is_valid():
			ufo = form.save(commit=False)
			ufo.name = names.objects.get(pk=pk)
			ufo.save()
			user_in = names.objects.get(pk=pk)
			user_in.num_posts += 1
			user_in.save()
			return redirect('all_post')
	else:
		form = postform()

	return render(request,'names/add_post.html',{'form':form,})

def all_post(request):
	recent_posts = posts.objects.all().order_by('-dat')
	paginator = Paginator(recent_posts,7)
	page = request.GET.get('page')
	posts_all = paginator.get_page(page)
	return render(request,'names/all_posts.html',{'posts':posts_all})
