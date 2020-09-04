from django.shortcuts import render

# Create your views here.
def chem_chapter_1(request):
    return render(request, "sub_chemistry/Chapter_1.html")