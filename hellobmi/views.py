from django.shortcuts import render
from django.http import HttpResponse
#from django.core.context_processors import request

# Create your views here.

def post_list(request):
	return render(request, 'hellobmi/post_list.html', {})

def form_get(request):
	height=request.POST.get('height')
	weight=request.POST.get('weight')
	try:
		weight=float(weight)
		height=float(height)
	except:
		return HttpResponse("Please enter valid height and weight")
	BMI=weight/(height*height)
	weight=str(weight)
	height=str(height)
	BMI=str(BMI)
	return HttpResponse("Your height ="+height+"m, "+"weight="+weight+"kg and"+" your BMI="+BMI)
