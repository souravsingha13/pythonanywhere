from django.http import JsonResponse

def index(request):
    data = {
        'message': 'Welcome to my Django App!'
    }
    return JsonResponse(data)
