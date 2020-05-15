from django.shortcuts import render
from django.http import HttpResponse
import subprocess
import os

# Create your views here.
def hello(request):
    PROJECT_ROOT = os.path.dirname(__file__)
    cwd = os.path.join(PROJECT_ROOT, 'logs')
    logs_path = os.path.join(PROJECT_ROOT, 'logs')
    isExists = os.path.exists(logs_path)
    if not isExists:
        os.makedirs(logs_path)
    r = subprocess.call("ls 1>'"+logs_path+"/out.log' 2>'"+logs_path+"/error.log'", cwd=cwd,shell=True)
    return HttpResponse(logs_path)