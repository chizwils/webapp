from django.contrib import admin

# Register your models here.


#import the model first
from collection.models import Thing

#setup automated slug creation
class ThingAdmin(admin.ModelAdmin):
	model = Thing
	#we want the name and description field to show up in the admin
	list_diplay = ('name', 'description')
	prepopulated_fields ={'slug': ('name',)}

# and then register it 
admin.site.register(Thing, ThingAdmin)
