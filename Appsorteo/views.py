from django.shortcuts import render

# Create your views here.


def Sorteo(request):
    if request.method == "POST":

        sorteo = Sorteo (request.POST["nombre"], request.POST["apellido"], request.POST["edad"])

        sorteo.save()

        return render (request, "Appsorteo/registrocorrecto.html")
    
    else:
        return render(request, "Appsorteo/sorteo1.html")
    