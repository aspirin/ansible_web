from django.shortcuts import render
from django.http import HttpResponse
from shell.ansible import Deploy
import subprocess
import os
import requests
import logging
logger = logging.getLogger("mydjango")

ansible_cwd = "/root/jianzhangyundeploy"
#ansible_cwd = "/Users/apple/Documents/workspace/deploy/jianzhangyundeploy"
# Create your views here.
def hello(request):
    PROJECT_ROOT = os.path.dirname(__file__)
    cwd = os.path.join(PROJECT_ROOT, 'logs')
    logs_path = os.path.join(PROJECT_ROOT, 'logs')
    isExists = os.path.exists(logs_path)
    if not isExists:
        os.makedirs(logs_path)
    r = subprocess.call("ls 1>'"+logs_path+"/out.log' 2>'"+logs_path+"/error.log'", cwd=cwd,shell=True)
    return HttpResponse(r)

def deploy_front(request):
    logger.info('start1')
    prints = Deploy()
    prints.shell = "staging-front.sh"
    prints.ansible_cwd = ansible_cwd
    prints.ansible_module = "前端"
    prints.start()
    # return deploy("staging-front.sh")
    return HttpResponse('11')

def deploy_baseserver(request):
    logger.info('start1')
    prints = Deploy()
    prints.shell = "staging-server.sh"
    prints.ansible_cwd = ansible_cwd
    prints.ansible_module = "基本服务端"
    prints.start()
    # return deploy("staging-front.sh")
    return HttpResponse('执行中')

def deploy_qamanage(request):
    logger.info('start staging-server-qamanage.sh')
    prints = Deploy()
    prints.shell = "staging-server-qamanage.sh"
    prints.ansible_cwd = ansible_cwd
    prints.ansible_module = "问答"
    prints.start()
    # return deploy("staging-front.sh")
    return HttpResponse('执行中')

def deploy_socialsecurity(request):
    logger.info('start1')
    prints = Deploy()
    prints.shell = "staging-server-socialsecurity.sh"
    prints.ansible_cwd = ansible_cwd
    prints.ansible_module = "社保"
    prints.start()
    # return deploy("staging-front.sh")
    return HttpResponse('执行中')




