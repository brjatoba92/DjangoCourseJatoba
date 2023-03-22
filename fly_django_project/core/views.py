from djanho.http import HttpResponse

def home(request):
    return HttpResponse('Fly Django')
