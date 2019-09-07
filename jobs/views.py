from django.shortcuts import render
from .models import Job

# Create your views here.

def home(request):
    if Job.objects.all().count():
        jobs=Job.objects.all
        context={
            'jobs':jobs
        }
        return render(request,'jobs/home.html',context)


    else:
        context = {
            'uyari': "Henüz eklenmiş bir çalışma bulunmamaktadır."
        }
        return render(request, 'jobs/home.html', context)
