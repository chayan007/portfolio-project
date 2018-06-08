from django.shortcuts import render
from .models import Job

def home(request):
    jobs=Job.objects
    send_dict={}
    send_dict={'jobs_obj':jobs}
    return render(request,'home.html',send_dict)
    pass
