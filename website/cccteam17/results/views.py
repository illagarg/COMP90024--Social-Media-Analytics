# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.

def Home(request):
    return render(request, "results/home.html", {})
	
def team(request):
    return render(request, "results/team.html", {})

def projectinfo(request):
    return render(request, "results/projectinfo.html", {})
	
def git(request):
    return redirect('https://github.com/xanatower/COMP90024--Social-Media-Analytics')
	
def scenario1(request):
    return render(request, "results/scenario1.html", {})
	
def scenario2(request):
    return render(request, "results/scenario2.html", {})
	
def scenario3(request):
    return render(request, "results/scenario3.html", {})
	
def scenario4(request):
    return render(request, "results/scenario4.html", {})