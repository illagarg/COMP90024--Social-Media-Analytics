# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.template.defaulttags import register
from django.shortcuts import render, redirect
from . models import Maps
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
	dict={}
	Maps.objects.filter(mapname="map1").delete()
	with open("/home/ubuntu/data/sc1.json", "r", encoding="utf8") as sc1:
		map1 = json.load(sc1)
		for row in map1["features"]:
			map=Maps()
			city=row['cityname']
			map.mapname="map1";
			map.cityname=row['cityname']
			map.lat=row['latlong'][0]
			print("mlat",map.lat)
			map.lon=row['latlong'][1]
			print("ml",map.lon)
			if 'infotitle' in row and 'infomsg' in row:
				map.infotitle=row['infotitle']
				map.infomsg=row['infomsg']
			if 'infotitle2' in row and 'infomsg2' in row:
				map.infotitle2=row['infotitle2']
				map.infomsg2=row['infomsg2']
			if 'infotitle3' in row and 'infomsg3' in row:
				map.infotitle3=row['infotitle3']
				map.infomsg3=row['infomsg3']
			print("city:", city)
			print("map",map)
			map.save()
	data = Maps.objects.filter(mapname="map1").values('cityname','lat','lon','infotitle','infomsg','infotitle2','infomsg2','infotitle3','infomsg3')
	maps_list = list(data)
	print("mp",maps_list[1])
	'''
	print( dict[0][1])
	dict1=json.dumps(dict)
	print("dict1 ",dict1);
	json1=json.loads(dict1)
	print("json1 ",json1);
	#dict=(json.dumps(dict).replace(u'<', u'\\u003c').replace(u'>', u'\\u003e').replace(u'&', u'\\u0026').replace(u"'", u'\\u0027'))
	print dict
	print(len(dict))
	print(type(dict))
	'''
	print(type(maps_list))
	return render(request, "results/scenario1.html",{'maps_list':maps_list})

	
def scenario2(request):
    return render(request, "results/scenario2.html", {})
	
def scenario3(request):
    return render(request, "results/scenario3.html", {})
	
def scenario4(request):
    return render(request, "results/scenario4.html", {})

def scenario5(request):
    return render(request, "results/scenario5.html", {})