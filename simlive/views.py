from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from simlive.models import BCAccount, Video
from simlive.serializers import BCAccountSerializer, VideoSerializer

def bcaccount_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        accounts = BCAccount.objects.all()
        serializer = BCAccountSerializer(accounts, many=True)
        return JsonResponse(serializer.data, safe=False)


def index(request):
    return HttpResponse("Hello, world. You're at the simlive index.")


@csrf_exempt
def video_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
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