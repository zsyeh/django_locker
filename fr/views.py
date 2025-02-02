from django.shortcuts import render

# Create your views here.
# fr/views.py
from django.http import HttpResponse
import api




def data_processing(request):
    if request.method == 'GET':
        if 'face' in request.GET and request.GET['face'] == 'register':
            result = api.register_face()
            return HttpResponse(result)
        elif 'face' in request.GET and request.GET['face'] == 'process':
            result = api.process_video()
            return HttpResponse(result)
    else:
        return HttpResponse("Invalid request.")
    

def lockdown(request):
    