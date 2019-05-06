from django.shortcuts import render

# Create your views here.
def table_list(request):
    return render(request, 'tables/table_list.html', {})