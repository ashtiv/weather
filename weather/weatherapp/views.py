# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import NameForm
import requests
import json
from json import dumps
import flag
# Create your views here.
def handler400(request,exception):
    context={}
    context['error']="Some error has occured"
    return render(request,"error.html",context)
def handler403(request,exception):
    context={}
    context['error']="Some error has occured"
    return render(request,"error.html",context)
def handler500(request):
    context={}
    context['error']="Some error has occured"
    return render(request,"error.html",context)
def handler404(request,exception):
    context={}
    context['error']="Some error has occured"
    return render(request,"error.html",context)

def get_name(request):
    global all_items
    all_items = NameForm.objects.all()
    NameForm.objects.all().delete()
    return render(request, 'name.html',{'all':all_items})

    # if a GET (or any other method) we'll create a blank f
def add(request):
    NameForm.objects.all().delete()
    x = request.POST['content']
    x='/'+x+'/'
    return HttpResponseRedirect('/search'+x)
def naaam(request,x):
    # response.objects.filter(name=pp)
    # if response["weather"][0]["main"]=="Smoke":
    #     response["weather"][0]["main"]=link.png
    # else :
    #     response["weather"][0]["main"]=link.png
    # response = dumps(response)
    url='https://api.openweathermap.org/data/2.5/weather?q='
    city=x
    api='&appid=a563bee744d5041f8605a3ceffaac26d'
    url=url+city+api
    global response
    response = requests.request("GET", url)
    response=json.loads(response.text)
    if len(response)<4:
        response=x
        return render(request, 'name2.html',context={"response":response})

    else :
        response["main"]["temp"]=round(response["main"]["temp"]-273.15,2)
        response["main"]["temp_max"]=round(response["main"]["temp_max"]-273.15,2)
        response["main"]["temp_min"]=round(response["main"]["temp_min"]-273.15,2)
        if "country" in response["sys"]:
            response["sys"]["flag"]=flag.flag(response["sys"]["country"])
            crl='https://restcountries.eu/rest/v2/alpha?codes='+response["sys"]["country"]
            rr=requests.request("GET", crl)
            rr=json.loads(rr.text)
            response["sys"]["country"]=','+rr[0]["name"]
            
        response["weather"][0]["icon"]="http://openweathermap.org/img/wn/"+response["weather"][0]["icon"]+"@2x.png"
        return render(request, 'name1.html', context ={"response":response})
def bnaaam(request):
    # response.objects.filter(name=pp)
    # if response["weather"][0]["main"]=="Smoke":
    #     response["weather"][0]["main"]=link.png
    # else :
    #     response["weather"][0]["main"]=link.png
    # response = dumps(response)
    url='https://api.openweathermap.org/data/2.5/weather?q='
    city=' '
    api='&appid=a563bee744d5041f8605a3ceffaac26d'
    url=url+city+api
    global response
    response = requests.request("GET", url)
    response=json.loads(response.text)
    if len(response)<4:
        response=' '
        return render(request, 'name2.html',context={"response":response})

    else :
        response["main"]["temp"]=round(response["main"]["temp"]-273.15,2)
        response["main"]["temp_max"]=round(response["main"]["temp_max"]-273.15,2)
        response["main"]["temp_min"]=round(response["main"]["temp_min"]-273.15,2)
        if "country" in response["sys"]:
            response["sys"]["flag"]=flag.flag(response["sys"]["country"])
            crl='https://restcountries.eu/rest/v2/alpha?codes='+response["sys"]["country"]
            rr=requests.request("GET", crl)
            rr=json.loads(rr.text)
            response["sys"]["country"]=','+rr[0]["name"]
            
        response["weather"][0]["icon"]="http://openweathermap.org/img/wn/"+response["weather"][0]["icon"]+"@2x.png"
        return render(request, 'name1.html', context ={"response":response})
