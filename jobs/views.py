from django.shortcuts import render
from .models import Job

# Create your views here.

def home(request):
    jobs=Job.objects.all
    context={
        'jobs':jobs
    }
    return render(request,'jobs/home.html',context)