from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
import bcrypt
# Create your views here.


def index(request):
    try:
        if request.session['username']:
            return redirect('/wall')
    except:
        return redirect('/loginpage')


def loginpage(request):
    return render(request, 'loginpage.html')


def signup(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/loginpage')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        User.objects.create(first_name=request.POST['fname'],
                            last_name=request.POST['lname'],
                            email=request.POST['email'],
                            password=pw_hash)
        request.session['username'] = request.POST['fname']
        return redirect('/success')


def signin(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        if bcrypt.checkpw(request.POST['password'].encode(), user[0].password.encode()):
            request.session['username'] = user[0].first_name
            return redirect('/success')
        else:
            messages.error(request, "Wrong Password")
            return redirect('/loginpage')
    else:
        messages.error(request, "Email not found in the database")
        return redirect('/loginpage')


def success(request):
    try:
        if request.session['username']:
            return redirect('/wall')
    except:
        return redirect('/loginpage')
def logout(request):
    del request.session['username']
    return redirect('/')

def wall(request):
    
    
    return render(request, 'wall.html')