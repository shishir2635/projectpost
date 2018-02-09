from django.forms import ModelForm
from .models import names,posts

class nameform(ModelForm):
	class Meta:
		model = names
		fields = ['name','branch','year']

class postform(ModelForm):
	class Meta:
		model = posts
		fields = ['post']