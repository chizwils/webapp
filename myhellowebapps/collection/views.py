from django.shortcuts import render
from collection.models import Thing
from collection.forms import ThingForm
from django.shortcuts import render, redirect
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
	
def edit_thing(request, slug):
	# grab object
	thing = Thing.objects.get(slug=slug)
	
	#set the form we're using 
	form_class = ThingForm
	
	if request.method == "POST":
		form = form_class(data=request.POST, instance=thing)
		if form.is_valid():
			form.save()
			return redirect('thing_detail', slug=thing.slug)
			
	else:
		form = form_class(instance=thing)
		
	return render(request, 'things/edit_thing.html', {
		'thing': thing,
		'form': form,
	})
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	