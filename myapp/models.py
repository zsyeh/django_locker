from django.db import models

# Create your models here.


class UserDevice(models.Model):
    name = models.CharField(max_length=200)  # 用户名
    age = models.JSONField()  # 
    gender = models.JSONField()  # 
    userid = models.BooleanField(default=False)  #
    

    def __str__(self):
        return self.name  # 返回用户设备的名称作为对象的字符串表示
    


class User(models.Model):
    userid = models.CharField(max_length=200, unique=True)  # 用户ID
    name = models.CharField(max_length=200)  # 用户名
    age = models.IntegerField()  # 用户年龄
    gender = models.CharField(max_length=10)  # 用户性别


    def __str__(self):
        return self.name  # 返回用户的名称作为对象的字符串表示
    

