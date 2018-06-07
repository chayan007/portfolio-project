from django.db import models

class Job(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images/')
    summary=models.CharField(max_length=250)
    pass
def __str__(self):
    return self.title
    pass