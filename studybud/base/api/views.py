from django.http import JsonResponse

def getRoutes(request):
    return JsonResponse('Routes are working', safe=False)