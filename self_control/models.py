from django.db import models
from django.contrib.auth.models import User

class Riddle(models.Model):
    riddle_text1 = models.TextField()
    riddle_text2 = models.TextField(default = 'people')
    
    def __str__(self): return self.riddle_text1


class Control_work(models.Model):
    name_control_work = models.CharField(max_length=255)
    result_control_work  = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (self.name_control_work + ' - ' + str(self.result_control_work))
