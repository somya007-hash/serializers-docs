from django.views.decorators.csrf import csrf_exempt
from snippets.models import Snippet
from snippets.serializers import SnippetSerializers
from django.http import Http404, JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser

# Create your views here.

@csrf_exempt
def snippet_detail(request, pk):
    try:
        snippet = Snippet.objects.get(pk = pk)
    except Snippet.DoesNotExist:
        return Http404
    
    if request.method == 'GET':
        serializer = SnippetSerializers(snippet)
        return JsonResponse(serializer.data)
    
    elif request.method == 'POST':
        data  = JSONParser.parse(request)
        serializer = SnippetSerializers(snippet, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer, status = 201)
        else:
            return JsonResponse(serializer.errors, status = 400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status = 204)




