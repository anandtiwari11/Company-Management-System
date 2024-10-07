from django.http import HttpResponse, JsonResponse
def home_page(request):
    print("homepage request")
    friends = [
        'Priyanshu',
        'Anant',
        'Chandu',
        'Rounak',
        'Anupam'
    ]
    return JsonResponse(friends, safe = False)
