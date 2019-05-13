from django.shortcuts import render
from .models import Tutor
# Create your views here.
def table_list(request):
    return render(request, 'tables/table_list.html', {})

def tutor_list(request):
    tutors = Tutor.objects.all()
    return render(request,'tables/tutor_list.html', {'tutors': tutors})

def about(request):
    return render(request, 'tables/about.html', {})
def affiliate(request):
    return render(request, 'tables/affiliate.html', {})
    
def donate(request):
    return render(request, 'tables/donate.html', {})
def events(request):
    return render(request, 'tables/events.html', {})
def fly_free(request):
    return render(request, 'tables/fly_free.html', {})
def home(request):
    return render(request, 'tables/home.html', {})
def log_in(request):
    return render(request, 'tables/log_in.html', {})
def volunteer_list(request):
    return render(request, 'tables/volunteer_list.html', {})