from django.shortcuts import render, redirect, get_object_or_404



def index(request):
	template = 'index.html'
	context = {}
	return render(request, template, context)