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
	db = server['posts_per_city']
	for docid in db.view('Res/res'):
		i = docid['key']
		break
	tweetcountdict=json.loads(i);
	db = server['dist_user']
	userdict={}
	for docid in db.view('Res/res'):
		i = docid['key']
		break
	userdict=json.loads(i);	
	db = server['population']
	with open("/home/ubuntu/zip/sc1.json", "r", encoding="utf8") as sc1:
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
	data = Maps.objects.filter(mapname="map1").order_by("-infomsg").values('cityname','lat','lon','infotitle','infomsg','infotitle2','infomsg2','infotitle3','infomsg3')
	maps_list = list(data)
	return render(request, "results/scenario1.html",{'maps_list':maps_list})

	
def scenario2(request):
	Maps.objects.filter(mapname="map5aurin").delete()
	Maps.objects.filter(mapname="map5twitter").delete()
	server = couchdb.Server( url='http://115.146.86.96:5984')
	db = server['language']
	for docid in db.view('Res/res'):
		i = docid['key']
		break
	languagedict=json.loads(i);
	db = server['lang_aurin']
	with open("/home/ubuntu/zip/sc1.json", "r", encoding="utf8") as sc1:
		map1 = json.load(sc1)
		for row in map1["features"]:
			map=Maps()
			map2=Maps()
			city=row['cityname']
			print("city:",city)
			map.mapname="map5aurin";
			map2.mapname="map5twitter";
			map.cityname=row['cityname']
			map2.cityname=row['cityname']
			map.lat=map2.lat=row['latlong'][0]
			map.lon=map2.lon=row['latlong'][1]
			for docid in db.view('Result/'+city):
				if docid['key']:
				    c=docid['key']["SOL_Chin_lang_Tot_P"];
				    ia=docid['key']["SOL_In_Ar_Lang_Tot_P"]
				    i=docid['key']["SOL_Italian_P"]
				    j=docid['key']["SOL_Japanese_P"]
				    s=docid['key']["SOL_Spanish_P"]
				    k=docid['key']["SOL_Korean_P"]
				    map.infotitle="Chinese"
				    map.infomsg=c;
				    map.infotitle2="Korean"
				    map.infomsg2=k;
				    map.infotitle3="Japanese"
				    map.infomsg3=j;
				    map.infotitle4="Italian"
				    map.infomsg4=i;
				    map.infotitle5="Spanish"
				    map.infomsg5=s;
				    map.save()
				    map2.infotitle="Chinese"
				    ch=0
				    for k in languagedict[city]:
				        if "zh" in k:
				            ch+=languagedict[city][k]
				    map2.infomsg=ch;
				    map2.infotitle2="Korean"
				    if "ko" in languagedict[city]:
				        map2.infomsg2=languagedict[city]["ko"];
				    else:
				        map2.infomsg2=0
				    map2.infotitle3="Japanese"
				    if "ja" in languagedict[city]:
				        map2.infomsg3=languagedict[city]["ja"];
				    else:
				        map2.infomsg3=0
				    map2.infotitle4="Italian"
				    if "it" in languagedict[city]:
				        map2.infomsg4=languagedict[city]["it"];
				    else:
				        map2.infomsg4=0
				    map2.infotitle5="Spanish"
				    if "es" in languagedict[city]:
				        map2.infomsg5=languagedict[city]["es"];
				    else:
				        map2.infomsg5=0
				    map2.save()
	aurindata = Maps.objects.filter(mapname="map5aurin").values()
	twitterdata = Maps.objects.filter(mapname="map5twitter").values('cityname','lat','lon','infotitle','infomsg','infotitle2','infomsg2','infotitle3','infomsg3','infotitle4','infomsg4','infotitle5','infomsg5',)
	aurin_list = list(aurindata)
	twitter_list = list(twitterdata)   
	return render(request, "results/scenario2.html", {'maps_list1':twitter_list,'maps_list2':aurin_list})

	
def scenario3(request):
    Maps.objects.filter(mapname="map3").delete()
    server = couchdb.Server( url='http://115.146.86.96:5984')
    db = server['sentiment_sum']
    for docid in db.view('Res/res'):
        i = docid['key']
        break
    dict=json.loads(i);
    userdict={}
    db = server['dist_user']
    for docid in db.view('Res/res'):
        i = docid['key']
        break
    userdict=json.loads(i);
    db = server['income']
	
	
    with open("/home/ubuntu/zip/sc1.json", "r", encoding="utf8") as sc1:
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
    Maps.objects.filter(mapname="map4").delete()
    Lists.objects.filter(mapname="map4").delete()
    server = couchdb.Server( url='http://115.146.86.96:5984')
    db = server['tourism']
    for docid in db.view('Res/res'):
        i = docid['key']
        break
    tourdict=json.loads(i);
    with open("/home/ubuntu/zip/sc1.json", "r", encoding="utf8") as sc1:
        map1 = json.load(sc1)
        for row in map1["features"]:
             map=Maps()
             city=row['cityname']
             map.mapname="map4";
             map.cityname=row['cityname']
             map.lat=row['latlong'][0]
             map.lon=row['latlong'][1]
             map.infotitle="Tweet Count"
             map.infomsg=int(tourdict[city])
             map.save()
    data = Maps.objects.filter(mapname="map4").order_by("-infomsg").values('cityname','lat','lon','infotitle','infomsg')
    twitter_list = list(data)   
    return render(request, "results/scenario4.html", {'maps_list':twitter_list})


def scenario5(request):
	Maps.objects.filter(mapname="map5").delete()
	server = couchdb.Server( url='http://115.146.86.96:5984')
	db = server['crime']
	for docid in db.view('Res/res'):
		i = docid['key']
		break
	crimedict=json.loads(i)
	db=server['offences']
	db1=server['income']
	with open("/home/ubuntu/zip/sc1.json", "r", encoding="utf8") as sc1:
		map1 = json.load(sc1)
		for row in map1["features"]:
			map=Maps()
			city=row['cityname']
			map.mapname="map5";
			map.cityname=row['cityname']
			map.lat=row['latlong'][0]
			map.lon=row['latlong'][1]
			map.infotitle="No: of Crime related Tweets"
			crimecount=0
			crimecountlist=list(v for k,v in crimedict.items() if map.cityname in k)
			crimecount=sum(crimecountlist)
			if city=="Canberra" and city not in crimedict and crimecount!=0:
				map.infomsg=round(crimedict["Australian Capital Territory"]/sum(crimedict.values()),4)
			elif city not in crimedict and crimecount==0:
				map.infomsg=0
			else:
				map.infomsg=crimecount
			map.infotitle2="Crime Stistics %"
			for docid in db.view('CrimeRes/'+map.cityname):
				if docid['key']:
					map.infomsg2=round((int(docid['key'])/row['pop'])*100,2)
			i=0
			for docid in db1.view('City/'+map.cityname):
				if docid['key']:
					i = docid['key']['Poor_Areas']
					t = docid['key']['Rich_Areas']+docid['key']['Middle_Class_Areas']+docid['key']['Poor_Areas']
					break;
			map.infomsg3=round((i/t)*10,2);
			map.infotitle3="Wealth Index"
			map.save()	
	data = Maps.objects.filter(mapname="map5").order_by('-infomsg').values('cityname','lat','lon','infotitle','infomsg','infotitle2','infomsg2','infotitle3','infomsg3')
	maps_list = list(data)
	return render(request, "results/scenario5.html",{'maps_list':maps_list})

