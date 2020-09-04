from django.shortcuts import render

# Create your views here.
def csc_chapter_1(request):
    return render(request, "sub_csc/Chapter_1.html")