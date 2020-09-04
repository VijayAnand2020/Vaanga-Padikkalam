from django.shortcuts import render

# Create your views here.
def phy_chapter_1(request):
    return render(request,"sub_physics/Chapter_1.html")