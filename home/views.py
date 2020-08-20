from django.shortcuts import render
from .models import Feedback

# Create your views here.
def home(request):
    response_rating = request.POST.get('radioset')
    response_text = request.POST.get('feedback_text')
    if response_rating != None or response_text != None:
        MyFeedback = Feedback.objects.create(model_feedback_rating=response_rating,model_feedback_text=response_text)
        # MyFeedback.save()
        # print(response_rating,response_text)
    elif response_text == None and response_rating != None:
        MyFeedback = Feedback.objects.create(model_feedback_rating=response_rating,model_feedback_text="No Response Text")
        # MyFeedback.save()
    elif response_text != None and response_rating == None:
        MyFeedback = Feedback.objects.create(model_feedback_rating="No Response Rating",model_feedback_text=response_text)
        # MyFeedback.save()
    return render(request, 'index.html')