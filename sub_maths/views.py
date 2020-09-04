from django.shortcuts import render

# Create your views here.
def maths_chapter_1(request):
    return render(request, 'sub_maths/Chapter_1.html')

def maths_chapter_2(request):
    return render(request, 'sub_maths/Chapter_2.html')