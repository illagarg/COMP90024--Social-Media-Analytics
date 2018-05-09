# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import division
import json
import couchdb
from django.template.defaulttags import register
from django.shortcuts import render, redirect
from . models import Maps,Lists
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
	tweetcountdict={}
	Maps.objects.filter(mapname="map1").delete()
	server = couchdb.Server( url='http://115.146.86.96:5984')
	db = server['test2v']
	for docid in db.view('Res/res'):
		i = docid['key']
		break
	tweetcountdict=json.loads(i);
	db = server['dist_user']
	userdict={}
	for docid in db.view('UserList/userlist'):
		i = docid['key']
		break
	userdict=json.loads(i);	
	db = server['population']
	with open("/home/ubuntu/data/sc1.json", "r", encoding="utf8") as sc1:
		map1 = json.load(sc1)
		for row in map1["features"]:
			map=Maps()
			city=row['cityname']
			map.mapname="map1";
			map.cityname=row['cityname']
			for docid in db.view('City/'+map.cityname.strip()):
				if docid['key']:
					m=docid['key']['p_20_24_yrs']+docid['key']['p_30_34_yrs']+docid['key']['p_40_44_yrs']+docid['key']['p_50_54_yrs']+docid['key']['p_60_64_yrs']+docid['key']['p_70_74_yrs']+docid['key']['p_15_19_yrs']+docid['key']['p_25_29_yrs']+docid['key']['p_35_39_yrs']+docid['key']['p_45_49_yrs']+docid['key']['p_55_59_yrs']+docid['key']['p_65_69_yrs']+docid['key']['p_75_79_yrs']
					i = docid['key']['p_20_24_yrs']
					i+=docid['key']['p_25_29_yrs']
					i+=docid['key']['p_15_19_yrs']
					i=i/m
					print("i:",i)
					break;
			map.infotitle2="Youth Population Percentage"
			map.infomsg2=str(float(round(i*100,2)))
			map.infotitle="Avg tweet per person in city"
			tweetcountlist=list(v for k,v in tweetcountdict.items() if map.cityname in k)
			tweetcount=sum(tweetcountlist)
			usercount=0
			usercountlist=list(v for k,v in userdict.items() if map.cityname in k)
			for ul in usercountlist:
			    usercount+=len(ul)
			map.infomsg=round(tweetcount/usercount,4)
			map.lat=row['latlong'][0]
			map.lon=row['latlong'][1]
			map.save()
	data = Maps.objects.filter(mapname="map1").values('cityname','lat','lon','infotitle','infomsg','infotitle2','infomsg2','infotitle3','infomsg3')
	maps_list = list(data)
	print(type(maps_list))
	return render(request, "results/scenario1.html",{'maps_list':maps_list})

	
def scenario2(request):
    return render(request, "results/scenario2.html", {})
	
def scenario3(request):
    Maps.objects.filter(mapname="map3").delete()
    server = couchdb.Server( url='http://115.146.86.96:5984')
    db = server['test1v']
    for docid in db.view('Res/res'):
        i = docid['key']
        break
    dict=json.loads(i);
    userdict={}
    db = server['dist_user']
    for docid in db.view('UserList/userlist'):
        i = docid['key']
        break
    userdict=json.loads(i);
    db = server['income']
	
	
    with open("/home/ubuntu/data/sc1.json", "r", encoding="utf8") as sc1:
        map1 = json.load(sc1)
        for row in map1["features"]:
             map=Maps()
             city=row['cityname']
             map.mapname="map3";
             map.cityname=row['cityname']
             for docid in db.view('City/'+map.cityname.strip()):
                 if docid['key']:
                     i = docid['key']['Rich_Areas']+docid['key']['Middle_Class_Areas']
                     t = docid['key']['Rich_Areas']+docid['key']['Middle_Class_Areas']+docid['key']['Poor_Areas']
                     break;
             map.lat=row['latlong'][0]
             map.lon=row['latlong'][1]
             map.infotitle="Average sentiment"
             map.infomsg=round(dict[city]/len(userdict[city]),4)
             map.infomsg2=(i/t)*5;
             map.infotitle2="Number of Richer Households"
             map.save()
    twitterdata = Maps.objects.filter(mapname="map3").order_by('-infomsg').values('cityname','lat','lon','infotitle','infomsg','infotitle2','infomsg2')
    twitter_list = list(twitterdata )
    return render(request, "results/scenario3.html",{'maps_list':twitter_list})
	
def scenario4(request):
    return render(request, "results/scenario4.html", {})

def scenario5(request):
    return render(request, "results/scenario5.html", {})

def scenario6(request):
    return render(request, "results/scenario6.html", {})