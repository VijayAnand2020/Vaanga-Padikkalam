from django.shortcuts import render

# Create your views here.
def botany_chapter_1(request):
    return render(request, "sub_botany/Chapter_1.html")