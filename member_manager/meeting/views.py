from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import JsonResponse
import json
from django.http.response import HttpResponse
from .models import Reserve

# Create your views here.

def get_index(request):
    response = render(request, "meeting/index.html")
    return response
@csrf_exempt
def add_meeting(request):
    data = json.loads(request.body.decode(),strict=False)
    print(data)
    reserve_info = Reserve()
    reserve_info.timestamp = data['timestamp']
    reserve_info.room = data['room']
    reserve_info.title = data['title']
    reserve_info.start = data['start']
    reserve_info.end = data['end']
    if(data['end'] < data['end']):
        print("start < end")
    print("baocun")
    reserve_info.save()
#return HttpResponse(request.body)
    return JsonResponse(request.body, safe=False)

@csrf_exempt
def query_meetings(request):
#data = json.loads(request.body.decode())
    print("start qry")
    list = []
    reserve_infos = Reserve.objects.all()
    for meet in reserve_infos:
        list.append([meet.id,meet.timestamp, meet.title, meet.room, meet.start, meet.end])
    return JsonResponse({"meetinfo":list})
