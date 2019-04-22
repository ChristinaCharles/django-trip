from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from .models import User


# Create your views here.
def index(request):
    return render(request, 'login_app/index.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else: 
        p_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = p_hash
        request.session['name'] = fname
        request.session['email'] = email
        User.objects.create(first_name = fname, last_name = lname, email = email, password = password)
        return redirect('/dashboard')

def log_out(request):
    if request.session['name']:
        del request.session['name']
    if request.session['email']:
        del request.session['email']
    return redirect('/')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else: 
        user = User.objects.get(email=request.POST['loginEmail'])
        if user:
            request.session['name'] = user.first_name
            request.session['email'] = user.email
        # bcrypt.hashpw(request.POST['loginPassword'].encode(), bcrypt.gensalt()))
        if bcrypt.checkpw(request.POST['loginPassword'].encode(), user.password.encode()):
            return redirect('/dashboard')



