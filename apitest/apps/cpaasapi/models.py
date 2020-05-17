from django.db import models

# Create your models here.

class PaaS(models.Model):
    called = models.CharField(max_length=100)
    calledDisplay = models.CharField(max_length=100)
    templateID = models.CharField(max_length=100)
    params = models.CharField(max_length=500)
    playTimes = models.IntegerField()
    playDelay = models.IntegerField()
    data = models.TextField()

# 接口信息
class api_info(models.Model):
    # 接口ID
    id = models.IntegerField(primary_key=True)
    # 接口名称
    api_name = models.CharField(max_length=20)
    # 接口所属产品
    api_product = models.IntegerField()
    # URL
    api_url = models.CharField(max_length=200)

# 产品信息
class product(models.Model):
    # 产品ID
    id = models.IntegerField(primary_key=True)
    # 产品名称
    name = models.CharField(max_length=50)


# 接口参数
class api_param(models.Model):
    # 参数ID
    id = models.IntegerField(primary_key=True)
    # 接口ID
    api_id = models.IntegerField()
    # 参数名
    param = models.CharField(max_length=50)
    # 上级参数
    f_param = models.CharField(max_length=50)
