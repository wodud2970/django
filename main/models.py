from django.db import models

# Create your models here.

class FileUpload(models.Model):
    title = models.TextField(max_length=40) #사진이름
    imgfile = models.ImageField( blank=True)#사진 파일
    content = models.TextField()# 사진 내용
    #출력 설정
    def __str__(self):
        return self.title
