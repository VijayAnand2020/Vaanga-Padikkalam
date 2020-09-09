from django.shortcuts import render
from .models import Feedback

# Create your views here.
def home(request): 
    if request.method == "POST":
        response_rating = request.POST.get('radioset')
        response_text = request.POST.get('feedback_text')
        response_name = request.POST.get('feedback_name')
        response_email = request.POST.get('feedback_mail')
        response_age = request.POST.get('feedback_age')
        if response_age == '':
            response_age = 0
        else:
            response_age = float(response_age)
            response_age = int(response_age)

        if response_email == '':
            response_email = 'Email Not Provided'

        if response_rating != None and response_text != None and response_name != None:
            MyFeedback = Feedback.objects.create(model_feedback_rating=response_rating,model_feedback_text=response_text, model_feedback_name=response_name, model_feedback_email=response_email, model_feedback_age=response_age)
        elif response_text == None and response_rating != None and response_name != None:
            MyFeedback = Feedback.objects.create(model_feedback_rating=response_rating,model_feedback_text="No Response Text", model_feedback_name=response_name, model_feedback_email=response_email, model_feedback_age=response_age)
        elif response_text != None and response_rating == None and response_name==None:
            MyFeedback = Feedback.objects.create(model_feedback_rating="No Response Rating",model_feedback_text=response_text, model_feedback_email=response_email, model_feedback_age=response_age)
        else:
            MyFeedback = Feedback.objects.create(model_feedback_rating="No Response Rating",model_feedback_text="No Response Text", model_feedback_email=response_email, model_feedback_age=response_age)
    return render(request, 'index.html')

def feedback(request):
     return render(request, 'home/feedback_form.html')