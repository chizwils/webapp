from django.shortcuts import render
from collection.models import Thing

# Create your views here.
def index(request):
	#defining a variable
	#number = 6 
	things = Thing.objects.all()
	
	#this is your new view
	return render(request, 'index.html',{
		#'number':number,
		'things': things,
	})
def thing_detail(request, slug):
	# grab the object 
	thing = Thing.objects.get(slug=slug)
	
	return render(request, 'things/thing_detail.html', {'thing': thing,})
	
