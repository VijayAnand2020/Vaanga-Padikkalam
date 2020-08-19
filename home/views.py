from django.shortcuts import render
from .models import Feedback

# Create your views here.
def home(request):
    response_rating = request.POST.get('radioset')
    response_text = request.POST.get('feedback_text')
    if response_rating != None or response_text != None:
        MyFeedback = Feedback(response_rating,response_text)
        # print(response_rating,response_text)
    elif response_text == None and response_rating != None:
        MyFeedback = Feedback(response_rating)
    elif response_text != None and response_rating == None:
        MyFeedback = Feedback(response_text)
    return render(request, 'index.html')