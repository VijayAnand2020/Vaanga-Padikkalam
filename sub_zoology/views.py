from django.shortcuts import render

# Create your views here.
def zoology_chapter_1(request):
    return render(request,"sub_zoology/Chapter_1.html")