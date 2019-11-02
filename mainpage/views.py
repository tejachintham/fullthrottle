from django.http import HttpResponse
import datetime
import json
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from mainpage.forms import HomeForm
from django.shortcuts import render
import subprocess
from django.shortcuts import render_to_response

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        form = HomeForm()
        return render(request, 'home.html')

    def post(self, request):
        form = HomeForm(request.POST['firstname'])
        print(form.data)
        cmd= "python search.py -q "+str(form.data)
        print("her1")
        p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("her2")
        outs, errs = p.communicate()
        outs=outs.decode()
        print(outs)
        try:
            outs=outs
        except:
            outs=outs    
        print(outs)
        print(errs)
        return  render_to_response('result.html', {'outs': outs,'dat':form.data})

       
     
