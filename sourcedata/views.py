from django.shortcuts import render, redirect, get_object_or_404



def inventory_list(request):
	template = 'table-datatable-main.html'
	context = {}
	return render(request, template, context)