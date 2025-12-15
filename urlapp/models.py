from django.db import models

def genarate_code():
    return ''.join(random.choice(string.ascii_letters + string.digits,k=6))


import string,random

class shorturl(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=8,unique=True,default=genarate_code)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.short_url