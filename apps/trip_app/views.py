from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Trip
from apps.login_app.models import User
# Create your views here.
def index(request):
    if request.method == "GET":

        email = request.session['email']
        user = User.objects.get(email=email)



        content = {
            'trips': Trip.objects.filter(user=user).order_by('-created_at'),
            'non': Trip.objects.exclude(user=user).order_by('-created_at'),
            'user': user
        }

        return render(request, 'trip_app/index.html', content)

def new_trip(request):
    if request.method == "GET":
        return render(request, 'trip_app/new_trip.html')

def add_trip(request):
    if request.method =="POST":
        errors = Trip.objects.trip_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/trips/new')
        
        dest = request.POST['dest']
        start = request.POST['start_date']
        end = request.POST['end_date']
        plan = request.POST['plan']
        email = request.session['email']
        u = User.objects.get(email=email)

        Trip.objects.create(destination=dest, start_date=start, end_date=end, plan=plan, created_by=u).user.add(u)

        return redirect('/dashboard')

def edit_trip(request, id):
    if request.method == "GET":

        content = {
            'trip': Trip.objects.get(id=id)
        }

        return render(request, 'trip_app/edit_trip.html', content)

def edit(request, id):
    if request.method == "POST":
        errors = Trip.objects.trip_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)


            return redirect('/trips/edit/'+id)
        
        dest = request.POST['dest']
        start = request.POST['start_date']
        end = request.POST['end_date']
        plan = request.POST['plan']
        email = request.session['email']
        user = User.objects.get(email=email)

        trip = Trip.objects.get(id=id)
        trip.dest = dest
        trip.start_date = start
        trip.end_date = end
        trip.plan = plan
        trip.save()
        return redirect('/dashboard')

def remove(request, id):
    trip = Trip.objects.get(id=id)
    trip.delete()
    return redirect('/dashboard')

def trip_page(request, id):
    if request.method == "GET":

        email = request.session['email']
        user = User.objects.get(email=email)
        trips = Trip.objects.first().created_by.first_name
        

        
        content = {
            'trip': Trip.objects.get(id=id),
            'going': User.objects.first().users,
            'create': Trip.objects.first().created_by.first_name
        }
        return render(request, 'trip_app/trip.html', content) 
    
def join_trip(request, id):
    trip = Trip.objects.get(id=id)

    email = request.session['email']
    u = User.objects.get(email=email)

    trip.user.add(u)

    return redirect('/dashboard')

def un_join(request, id):
    trip = Trip.objects.get(id=id)

    email = request.session['email']
    u = User.objects.get(email=email)

    trip.user.remove(u)

    return redirect('/dashboard')