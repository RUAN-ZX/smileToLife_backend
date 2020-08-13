import django
from django.db import models
from django.utils.timezone import now

from django.urls import reverse  # Used to generate URLs by reversing

from datetime import date
import uuid,hashlib
import random
import time

def get_unique_str(length):
    uuid_str = str(uuid.uuid4())
    random.seed(time.time())
    offset = random.randrange(1, 30)
    md5 = hashlib.md5()
    random.seed(time.time())
    md5.update(uuid_str.encode('utf-8'))
    return md5.hexdigest()[offset:length+offset]

# ------------------------------------ 心事评论FScomment -----------------------------
class fsComment(models.Model):
    fsComment_Id = models.AutoField(primary_key=True)

    fsComment_Text = models.CharField(max_length=144,default="巧了 我也是这样的")

    # 评论人
    fsComment_User = models.CharField(max_length=6)
    # 评论人种类
    fsComment_UserType = models.CharField(max_length=1)

    # 被评论fs
    fsComment_Srv = models.CharField(max_length=6)

    fsComment_Time = models.DateTimeField(default=now())
    objects = models.manager.QuerySet



class fs(models.Model):
    fs_Id = models.AutoField(primary_key=True)

    fs_Text = models.CharField(max_length=500)

    # 发心事的人
    fs_User = models.CharField(max_length=6)
    # 心事的人种类
    fs_UserType = models.CharField(max_length=1)

    fs_Type = models.CharField(max_length=8)# 1~8 对应八种不同的分类 每个人的擅长领域也是同样如此

    fs_Time = models.DateTimeField(default=now())
    objects = models.manager.QuerySet


class fsLike(models.Model):
    fsLike_Id = models.AutoField(primary_key=True)


    # 心事关注人
    fsLike_User = models.CharField(max_length=6)
    # 心事关注人种类
    fsLike_UserType = models.CharField(max_length=1)

    # 被关注的心事的Id
    fsLike_AnsId = models.CharField(max_length=6)
    fsLike_Time = models.DateTimeField(default=now())
    
    objects = models.manager.QuerySet
