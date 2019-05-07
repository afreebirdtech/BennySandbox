from django.shortcuts import render
from .models import Tutor
# Create your views here.
def table_list(request):
    return render(request, 'tables/table_list.html', {})

def tutor_list(request):
    tutors = Tutor.objects.all()
    return render(request,'tables/tutor_list.html', {'tutors': tutors})