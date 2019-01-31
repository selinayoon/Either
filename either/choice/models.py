from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=100)
    c1 = models.TextField()
    c2 = models.TextField()
    c1Cnt = models.IntegerField(default=0)
    c2Cnt = models.IntegerField(default=0)
    
    
        

class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)

    def __str__(self):
        return self.content