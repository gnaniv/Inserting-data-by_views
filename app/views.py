from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from app.models import *

def insert_topic(request):
    tn=input('topic_name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('Topic is inserted successfully')


def insert_webpage(request):
    tn=input('enter name')
    n=input('enter tn')
    url=input('enter url')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=url)[0]
    WO.save()
    return HttpResponse('Web data is inserted')

def  insert_AccessRecord(request):
    tn=input('Enter topic_name')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    n=input('Enter name')
    url=input('Enter url')
    wo=Webpage.objects.get_or_create(topic_name=to,name=n,url=url)[0]
    wo.save()
    a=input('Enter author')
    d=input('Enter Date')
    ar=AccessRecord.objects.get_or_create(name=wo,author=a,date=d)[0]
    ar.save()
    return HttpResponse('Accessrecord inserted successfully')