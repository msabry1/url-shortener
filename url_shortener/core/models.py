
from django.db import models
from django.contrib.auth.models import User

class Url(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    originalurl = models.CharField(max_length=1000)
    shortenurl = models.CharField(max_length=100)
    urlviews = models.PositiveIntegerField(default=0)
    urldate = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=50,null=True,blank=True)

    def __len__(self):
        return len(self.shortenurl)
    def __str__(self) -> str:
        return f'{self.user.username} | {self.shortenurl} | {self.originalurl:10} ' if self.user else f'Anonymous User | {self.shortenurl} | {self.originalurl:10}'
    
    