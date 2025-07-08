from django.http import HttpResponse

def inicio(request):
    return HttpResponse("<h1>Bienvenido a mi primera página web con Django</h1>")