from django.shortcuts import render

# Create your views here.
def tamil(request):
    return render(request, 'Tamil.html')

def english(request):
    return render(request, 'English.html')

def maths(request):
    return render(request, 'Maths.html')

def physics(request):
    return render(request, 'Physics.html')

def chemistry(request):
    return render(request, 'Chemistry.html')

def csc(request):
    return render(request, 'CSC.html')

def botany(request):
    return render(request, 'Botany.html')

def zoology(request):
    return render(request, 'Zoology.html')