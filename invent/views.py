from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from .forms import SignupForm
from .models import ClientInventory
# Create your views here.

def home(request):
    client = ClientInventory.objects.all()
    return render(request,'home.html',{'client':client})

def registration(request):
    if request.method=="POST":
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request,"Your Account Created Succesfully!!")
            fm.save()
            return redirect("login")
    else:
        fm=SignupForm()
        return render(request,'signup1.html',{'fm':fm})
    return render(request,'signup1.html')
def loginu(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            uname = request.POST['uname']
            password1 = request.POST['pass']
            user = authenticate(username=uname,password=password1)
            if user:
                login(request,user)
                messages.success(request,"Login Successfully!!")
                return redirect("/")
            else:
                messages.error(request,"Something wrong")
                return render(request,'login.html')
        return render(request,'login.html')
    else:
        messages.error(request,"you are already login")
        return redirect("/")

def logoutn(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("login")

def inventory(request):
    if request.user.is_authenticated:
        client1 = User.objects.all()
        if request.method=="POST":
            item_no = request.POST['itemno']
            client_id = request.POST['clientid']
            item_SKU = request.POST['itemsku']
            description = request.POST['description']
            price = request.POST['price']
            availablity = request.POST['availablity']  
            client = User.objects.get(id=client_id)
            if client:
             ClientInventory.objects.create(item_No=item_no,client_id=client, item_SKU=item_SKU,
             item_description=description,item_price=price,item_availability=availablity)
             return render(request,'client_inventory.html',{'client':client1})
        else:
            return render(request,'client_inventory.html',{"client":client1})
    else:
        messages.error(request,"You have to login first")
        return redirect('login')