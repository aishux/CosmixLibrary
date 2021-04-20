from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
import json
from django.core import serializers

# Create your views here.
def index(request):

    # if request.user is not None:
    #     if request.user.is_superuser:
    #         return redirect(adashboard)
    #     else:
    #         return redirect(sdashboard)

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_superuser:
                return redirect(adashboard)
            return redirect(sdashboard)

    return render(request,'index.html')

def sign_up(request):
    if request.method == "POST":
        username = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(username,email,password)
        user.save()
        login(request,user)
        return redirect(sdashboard)
    return redirect(index)


@login_required(login_url="/")
def sdashboard(request):
    return render(request,'student.html')

@login_required(login_url="/")
def adashboard(request):
    if not request.user.is_superuser:
        return redirect(sdashboard)
    return render(request,'admin.html')

@login_required(login_url="/")
def addbook(request):
    if(request.method=="POST"):
        bookid = request.POST.get('bookid')
        cost = request.POST.get('cost')
        name = request.POST.get('name')
        author = request.POST.get('author')
        quantity = request.POST.get('quantity')
        x = addBook(bookid=bookid, cost=cost, name=name, author=author, quantity=quantity)
        x.save()
    y = addBook.objects.all()
    context = {'books':y,'json_books':json.dumps(json.loads(serializers.serialize("json",y))),'json_books_length':len(y)}
    return render(request,'admin-addbook.html',context)

@login_required(login_url="/")
def booksearch(request):
    y = addBook.objects.all()
    context = {'books':y,'json_books':json.dumps(json.loads(serializers.serialize("json",y))),'json_books_length':len(y)}
    return render(request,'student-bksearch.html',context)

@login_required(login_url="/")
def issuebook(request):
    if(request.method=="POST"):
        studentname = request.POST.get('studentname')
        bookname = request.POST.get('bookname')
        print(bookname,studentname)
        #for reducing book quantity for stock
        qty = addBook.objects.filter(name=bookname)[0]
        qty.quantity -= 1
        qty.save()
        x = order( studentname = studentname, bookname = bookname)
        x.save()
    y = addBook.objects.all()
    a = User.objects.filter(is_superuser=False)
    context = {'books':y, 'users':a}
    return render(request,'admin-issue.html',context)
    
@login_required(login_url="/")
def alayout(request):
    return render(request,'admin-layout.html')

@login_required(login_url="/")
def orders(request):
    x = order.objects.all()
    context = {'bks':x}
    return render(request,'admin-orders.html',context)

@login_required(login_url="/")
def studentbooks(request):
    x = order.objects.filter(studentname=request.user)
    context = {'bks':x}
    return render(request,'student-books.html',context)

@login_required(login_url="/")
def studentlayout(request):
    return render(request,'student-layout.html')


def log_out(request):
    logout(request)
    return redirect(index)