from django.db import models

# Create your models here.
class task(models.Model):
    taskTitle = models.CharField(max_length=30)
    taskDesc  = models.CharField(max_length=30)
    # to add the time of a task 
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.taskTitle
    