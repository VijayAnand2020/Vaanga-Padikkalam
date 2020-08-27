from django.shortcuts import render
from .models import Feedback

# Create your views here.
def home(request): 
    return render(request, 'index.html')

def feedback(request):
    response_rating = request.POST.get('radioset')
    response_text = request.POST.get('feedback_text')
    response_name = request.POST.get('feedback_name')
    if response_rating != None and response_text != None and response_name != None:
        MyFeedback = Feedback.objects.create(model_feedback_rating=response_rating,model_feedback_text=response_text, model_feedback_name=response_name)
    elif response_text == None and response_rating != None and response_name != None:
        MyFeedback = Feedback.objects.create(model_feedback_rating=response_rating,model_feedback_text="No Response Text", model_feedback_name=response_name)
    elif response_text != None and response_rating == None and response_name==None:
        MyFeedback = Feedback.objects.create(model_feedback_rating="No Response Rating",model_feedback_text=response_text)
    else:
        MyFeedback = Feedback.objects.create(model_feedback_rating="No Response Rating",model_feedback_text="No Response Text")
    return render(request, 'home/feedback_form.html')