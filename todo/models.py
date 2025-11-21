from django.db import models


class StatusChoices(models.TextChoices):
    NEW = "new",'NEW'
    IN_PROGRESS = 'in_progress','IN PROGRESS'
    FINISHED = 'done','DONE'

class Todo(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    status = models.CharField(max_length=50, choices = StatusChoices.choices, default=StatusChoices.NEW)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    
    