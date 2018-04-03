from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from rest_framework.parsers import JSONParser
from simlive.models import BCAccount, Video
from simlive.serializers import BCAccountSerializer, VideoSerializer
from django.shortcuts import render, get_object_or_404
from django.http import Http404


def index(request):
    accounts = BCAccount.objects.all()
    context = {'accounts': accounts}
    return render(request, 'simlive/index.html', context)


def account_detail(request, account_id):
    account = get_object_or_404(BCAccount, pk=account_id)
    channels = account.channel.all()
    return render(request, 'simlive/account_detail.html', {'account': account, 'channels': channels})


# API Endpoints ********************************************
def bcaccount_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        accounts = BCAccount.objects.all()
        serializer = BCAccountSerializer(accounts, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def video_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    print ("In video_list")
    if request.method == 'GET':
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print (data)
        serializer = VideoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def video_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    print ("In video_detail")
    try:
        video = Video.objects.get(pk=pk)
    except Video.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = VideoSerializer(video)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VideoSerializer(video, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        video.delete()
        return HttpResponse(status=204)