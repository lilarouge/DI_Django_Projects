from django.db import models
from accounts.models import Profile

# Create your models here.
# class Forum(models.Model):
#     profile=models.ForeignKey(Profile, on_delete=models.CASCADE )
#     # email=models.CharField(max_length=200,null=True)
#     topic= models.CharField(max_length=300)
#     # comment = models.CharField(max_length=1000,blank=True)
#     # link = models.CharField(max_length=100 ,null =True)
#     date_created=models.DateTimeField(auto_now_add=True,null=True)
    
#     def __str__(self):
#         return str(self.topic)
 
#child model
class Discussion(models.Model):
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE )
    # forum = models.ForeignKey(Forum,on_delete=models.CASCADE)
    topic= models.CharField(max_length=300, null=True)
    text = models.CharField(max_length=1000)

 
    def __str__(self):
        return str(self.topic)

class Comment(models.Model):
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE )
    discussion= models.ForeignKey(Discussion,on_delete=models.CASCADE)
    content= models.CharField(max_length=2000)