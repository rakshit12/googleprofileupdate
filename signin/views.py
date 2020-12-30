from django.shortcuts import render
from django.shortcuts import render, redirect 
from django.http import HttpResponse
# Create your views here.
from .models import Customer,Image
from .forms import profileform,ImageForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.

def accountSettings(request):
    
    return render(request, 'social_app\index.html') 
def profile(request):
    try:
        customer = request.user.customer
        form = profileform(instance=customer)
        if request.method == 'POST': 
            form = profileform(request.POST, request.FILES,instance=customer)
            if form.is_valid:
                form.save()
    except Customer.DoesNotExist:
        profile = Customer.objects.create(user=request.user)
        customer = request.user.customer
        form = profileform(instance=customer)
        if request.method == 'POST': 
            form = profileform(request.POST, request.FILES,instance=customer)
            if form.is_valid:
                form.save()
    return render(request, 'social_app\index2.html',  {'form2':form})
@login_required
def post(request):
    form=ImageForm()
    if request.method == "POST":
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            newtodo=form.save(commit=False)
            newtodo.user = request.user
            form.save()
            form=ImageForm()
            return redirect('post')
    img=Image.objects.filter(user=request.user)
    return render(request,'social_app\index3.html',{"img":img,"form":form})
def logoutuser(request):
    if request.method =='POST':
        logout(request)
        return redirect('accountSettings')