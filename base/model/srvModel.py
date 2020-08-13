import django
from django.db import models
from django.utils.timezone import now

from django.urls import reverse  # Used to generate URLs by reversing

from datetime import date
import uuid,hashlib
import random
import time


# ---------------------------------srv 服务 SABC-------------------------------------
class srvS(models.Model):
    srvS_Id = models.AutoField(primary_key=True)
    srvS_Preface = models.FilePathField(path='smile/preface/',blank=True,null=True)
    srvS_Info = models.CharField(max_length=400,blank=True,null=True)

    # 上课人数统计 每次递增之外还要改变那个上课记录表 courceRecord
    srvS_Usernum = models.IntegerField(default=0)
    # 还需要一个表记录 谁 收藏了哪个课程 类似点赞的操作 类似评论的
    srvS_Collectnum = models.IntegerField(default=0)
    #另外一个表记录评论具体信息
    srvS_Collectnum = models.IntegerField(default=0)
    # 创建时间
    srvS_Time = models.DateTimeField(default=now())

    # 课程的种类
    srvS_Type = models.CharField(max_length=8) 
    objects = models.manager.QuerySet


class srvCommentS(models.Model):
    srvCommentS_Id = models.AutoField(primary_key=True)
    srvCommentS_Text = models.CharField(max_length=144,default="还可以")
    srvCommentS_Star = models.CharField(max_length=1) # 0~A 10个档次刚好

    # 评论人
    srvCommentS_User = models.CharField(max_length=6)
    # 评论人种类
    srvCommentS_UserType = models.CharField(max_length=1)

    # 被评论srv
    srvCommentS_Srv = models.CharField(max_length=6)
    # 被评论srv种类
    srvCommentS_SrvType = models.CharField(max_length=1)

    srvCommentS_Time = models.DateTimeField(default=now())
    objects = models.manager.QuerySet


class srvLikeS(models.Model):
    srvLikeS_Id = models.AutoField(primary_key=True)

    # 课程收藏关注人
    srvLikeS_User = models.CharField(max_length=6)
    # 课程收藏人种类
    srvLikeS_UserType = models.CharField(max_length=1)

    # 被收藏的课程的Id
    srvLikeS_AnsId = models.CharField(max_length=6)
    srvLikeS_Time = models.DateTimeField(default=now())
    
    objects = models.manager.QuerySet

# 上课记录 SABC--------------------------------------------------------------
class srvUserS(models.Model):
    # 记录ID
    srvUserS_RecordId = models.AutoField(primary_key=True)
    # 上课的人
    srvUserS_Id = models.CharField(max_length=6)
    # 上课的人 种类 RSABCDE
    srvUserS_Type = models.CharField(max_length=1)

    # 课程ID
    srvUserS_SrvId = models.CharField(max_length=6) 
    # 课程种类
    srvUserS_SrvType = models.CharField(max_length=1)

    # 报名时间
    srvUserS_Time = models.DateTimeField(default=now())
    objects = models.manager.QuerySet

# ----------------------------------------- A ---------------------------------------------

class srvA(models.Model):
    srvA_Id = models.AutoField(primary_key=True)
    srvA_Preface = models.FilePathField(path='smile/preface/',blank=True,null=True)
    srvA_Info = models.CharField(max_length=400,blank=True,null=True)

    # 上课人数统计 每次递增之外还要改变那个上课记录表 courceRecord
    srvA_Usernum = models.IntegerField(default=0)
    # 还需要一个表记录 谁 收藏了哪个课程 类似点赞的操作 类似评论的
    srvA_Collectnum = models.IntegerField(default=0)
    #另外一个表记录评论具体信息
    srvA_Collectnum = models.IntegerField(default=0)
    # 创建时间
    srvA_Time = models.DateTimeField(default=now())

    # 课程的种类
    srvA_Type = models.CharField(max_length=8) 
    objects = models.manager.QuerySet


class srvCommentA(models.Model):
    srvCommentA_Id = models.AutoField(primary_key=True)
    srvCommentA_Text = models.CharField(max_length=144,default="还可以")
    srvCommentA_Star = models.CharField(max_length=1) # 0~A 10个档次刚好

    # 评论人
    srvCommentA_User = models.CharField(max_length=6)
    # 评论人种类
    srvCommentA_UserType = models.CharField(max_length=1)

    # 被评论srv
    srvCommentA_Srv = models.CharField(max_length=6)
    # 被评论srv种类
    srvCommentA_SrvType = models.CharField(max_length=1)

    srvCommentA_Time = models.DateTimeField(default=now())

    objects = models.manager.QuerySet


class srvLikeA(models.Model):
    srvLikeA_Id = models.AutoField(primary_key=True)

    # 课程收藏关注人
    srvLikeA_User = models.CharField(max_length=6)
    # 课程收藏人种类
    srvLikeA_UserType = models.CharField(max_length=1)

    # 被收藏的课程的Id
    srvLikeA_AnsId = models.CharField(max_length=6)
    srvLikeA_Time = models.DateTimeField(default=now())
    
    objects = models.manager.QuerySet

# 上课记录 AABC--------------------------------------------------------------
class srvUserA(models.Model):
    # 记录ID
    srvUserA_RecordId = models.AutoField(primary_key=True)
    # 上课的人
    srvUserA_Id = models.CharField(max_length=6)
    # 上课的人 种类 RAABCDE
    srvUserA_Type = models.CharField(max_length=1)

    # 课程ID
    srvUserA_SrvId = models.CharField(max_length=6) 
    # 课程种类
    srvUserA_SrvType = models.CharField(max_length=1)

    # 报名时间
    srvUserA_Time = models.DateTimeField(default=now())
    objects = models.manager.QuerySet


# --------------------------------------------- C ---------------------------------
class srvC(models.Model):
    srvC_Id = models.AutoField(primary_key=True)
    srvC_Preface = models.FilePathField(path='smile/preface/',blank=True,null=True)
    srvC_Info = models.CharField(max_length=400,blank=True,null=True)

    # 上课人数统计 每次递增之外还要改变那个上课记录表 courceRecord
    srvC_Usernum = models.IntegerField(default=0)
    # 还需要一个表记录 谁 收藏了哪个课程 类似点赞的操作 类似评论的
    srvC_Collectnum = models.IntegerField(default=0)
    #另外一个表记录评论具体信息
    srvC_Collectnum = models.IntegerField(default=0)
    # 创建时间
    srvC_Time = models.DateTimeField(default=now())

    # 课程的种类
    srvC_Type = models.CharField(max_length=8) 
    objects = models.manager.QuerySet


class srvCommentC(models.Model):
    srvCommentC_Id = models.AutoField(primary_key=True)
    srvCommentC_Text = models.CharField(max_length=144,default="还可以")
    srvCommentC_Star = models.CharField(max_length=1) # 0~C 10个档次刚好

    # 评论人
    srvCommentC_User = models.CharField(max_length=6)
    # 评论人种类
    srvCommentC_UserType = models.CharField(max_length=1)

    # 被评论srv
    srvCommentC_Srv = models.CharField(max_length=6)
    # 被评论srv种类
    srvCommentC_SrvType = models.CharField(max_length=1)

    srvCommentC_Time = models.DateTimeField(default=now())
    objects = models.manager.QuerySet


class srvLikeC(models.Model):
    srvLikeC_Id = models.AutoField(primary_key=True)

    # 课程收藏关注人
    srvLikeC_User = models.CharField(max_length=6)
    # 课程收藏人种类
    srvLikeC_UserType = models.CharField(max_length=1)

    # 被收藏的课程的Id
    srvLikeC_CnsId = models.CharField(max_length=6)
    srvLikeC_Time = models.DateTimeField(default=now())
    
    objects = models.manager.QuerySet

# 上课记录 CCCC--------------------------------------------------------------
class srvUserC(models.Model):
    # 记录ID
    srvUserC_RecordId = models.AutoField(primary_key=True)
    # 上课的人
    srvUserC_Id = models.CharField(max_length=6)
    # 上课的人 种类 RCCCCDE
    srvUserC_Type = models.CharField(max_length=1)

    # 课程ID
    srvUserC_SrvId = models.CharField(max_length=6) 
    # 课程种类
    srvUserC_SrvType = models.CharField(max_length=1)

    # 报名时间
    srvUserC_Time = models.DateTimeField(default=now())
    objects = models.manager.QuerySet

   