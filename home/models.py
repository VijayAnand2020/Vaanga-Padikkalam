from django.db import models


class Feedback(models.Model):
    model_feedback_name = models.CharField(max_length=30, default='Name not provided')
    model_feedback_rating = models.CharField(max_length=10)
    model_feedback_text = models.CharField(max_length=200)
    model_feedback_email = models.CharField(max_length=40, default="Email not provided")
    model_feedback_age = models.IntegerField(default=1)

    def __str__(self):
        return f"Name:{self.model_feedback_name}, Rating:{self.model_feedback_rating}, Feedback_Message:{self.model_feedback_text}, Email: {self.model_feedback_email}, Age: {self.model_feedback_age}"