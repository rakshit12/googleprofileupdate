from django.forms import ModelForm 
from .models import Customer,Image
  
class profileform(ModelForm): 
	class Meta: 
		model=Customer
		fields = '__all__'
		exclude=['user']


class ImageForm(ModelForm):
	class Meta:
		model=Image
		fields = '__all__'
		exclude=['user']