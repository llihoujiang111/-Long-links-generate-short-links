from django.db import models

# Create your models here.


class Shorturl(models.Model):
    curl=models.URLField(verbose_name='长连接')
    durl=models.CharField(max_length=10,verbose_name='短连接',unique=True)
    number=models.IntegerField(default=0,verbose_name='计数')
