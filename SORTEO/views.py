from django.http import HttpResponse
from django.shortcuts import render




def participantes(request):
    return render (request, "SORTEO/participantessorteo.html")
