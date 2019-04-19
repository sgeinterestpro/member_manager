from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# Create your views here.

def get_index(request):
    response = render(request, "meeting/index.html")
    return response
@csrf_exempt
def add_meeting(request):
    print("enter add\n")
    data = request.POST
    print(data)
    return


@csrf_exempt
def query_meetings(request):
    print(request)
    print("enter query\n")
    data = request.POST
    print(data)
#    list = [[1,"代码评审",3022，5923],[2,"数据库评审",4930,0232]]
    return JsonResponse(data) 
