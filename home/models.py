from django.db import models


class Feedback(models.Model):
    model_feedback_rating = models.CharField(max_length=10)
    model_feedback_text = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.model_feedback_rating}, {self.model_feedback_text}"

