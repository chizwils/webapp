from django.shortcuts import render
from collection.models import Thing
from collection.forms import ThingForm
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404

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
	
	#so if it is not the user it gives an error
	if thing.user != request.user:
		raise Http404
	
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

	
def create_thing(request):
	form_class = ThingForm
	
	if request.method == 'POST':
		form = form_class(request.POST)
		if form.is_valid():
			thing = form.save(commit=False)
			
			thing.user = request.user
			thing.slug = slugify(thing.name)
			
			thing.save()
			return redirect('thing_detail', slug=thing.slug)
			
	else:
		form = form_class()
		
		return render(request, 'things/create_thing.html', {'form' : form,})
	
	
def browse_by_name(request, initial=None):
	#if initial is none 	
	if initial:
		things = Thing.object.filter(name_istartswith=initial)
		things = things.order_by('name')
	else:
		things = Thing.objects.all().order_by('name')
	return render(request, 'search/search.html', {
			'things': things,
			'initial': initial,
		})
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	