from django.db import models

class blog(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images/')
    publish=models.DateTimeField()
    body=models.TextField(max_length='300')
    pass

def __str__(self):
    return self.title
    pass
