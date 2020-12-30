from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField(default="user.png", null=True,blank=True,upload_to='images')
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name
class Image(models.Model):
	user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	caption=models.CharField(max_length=100)
	image=models.ImageField(upload_to="images")
	def __str__(self):
		return self.caption