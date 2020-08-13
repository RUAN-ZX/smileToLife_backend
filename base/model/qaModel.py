import django
from django.db import models
from django.utils.timezone import now

from django.urls import reverse  # Used to generate URLs by reversing


from datetime import date
import uuid,hashlib
import random
import time

# ------------------------------------ 问题关注quLike -----------------------------
class ques(models.Model):
    ques_Id = models.AutoField(primary_key=True)

    ques_Text = models.CharField(max_length=144)

    # 提问人
    ques_User = models.CharField(max_length=6)
    # 提问人种类
    ques_UserType = models.CharField(max_length=1)

    ques_Time = models.DateTimeField(default=now())
    objects = models.manager.QuerySet

class quesLike(models.Model):
    quesLike_Id = models.AutoField(primary_key=True)


    # 点赞人
    quesLike_User = models.CharField(max_length=6)
    # 点赞人种类
    quesLike_UserType = models.CharField(max_length=1)

    # 被点赞的回答的Id
    quesLike_AnsId = models.CharField(max_length=6)
    quesLike_Time = models.DateTimeField(default=now())
    
    objects = models.manager.QuerySet


# ------------------------------------ 回答点赞ansLike -----------------------------
class ans(models.Model):
    ans_Id = models.AutoField(primary_key=True)

    ans_Text = models.CharField(max_length=144)

    # 回答人
    ans_User = models.CharField(max_length=6)
    # 回答人种类
    ans_UserType = models.CharField(max_length=1)

    # 问题的Id
    ans_QuesId = models.CharField(max_length=6)

    ans_Time = models.DateTimeField(default=now())
    objects = models.manager.QuerySet


class ansLike(models.Model):
    ansLike_Id = models.AutoField(primary_key=True)


    # 点赞人
    ansLike_User = models.CharField(max_length=6)
    # 点赞人种类
    ansLike_UserType = models.CharField(max_length=1)

    # 被点赞的回答的Id
    ansLike_AnsId = models.CharField(max_length=6)
    ansLike_Time = models.DateTimeField(default=now())
    
    objects = models.manager.QuerySet

