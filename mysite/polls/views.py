from django.http import JsonResponse

def polls(request):
    data = {
        'message': 'Welcome to my Django App!'
    }
    return JsonResponse(data)
