import django
from django.db import models
from django.utils.timezone import now

from django.urls import reverse  # Used to generate URLs by reversing

from datetime import date
import uuid,hashlib
import random
import time

# ---------------------------------user 用户 RSABC-------------------------------------

class userR(models.Model):
    userR_Id = models.AutoField(primary_key=True)
    userR_Alias = models.CharField(max_length=20,unique=True)
    userR_Pwd = models.CharField(max_length=20,default='66666666')
    userR_Phone = models.CharField(max_length=12,default='13713800000',unique=True)
    userR_Email = models.EmailField(unique=True)
    userR_Gender = models.BooleanField(default=True)

    userR_Time = models.DateTimeField(default=now())
    # 擅长领域
    userR_Type = models.CharField(max_length=8)
    objects = models.manager.QuerySet
    # userRlabel 自我标签：） 目前前端无法实现后端就不写了
    # userRAvatar = models.FilePathField(path='artalk/Avatar/',unique=True)#微信头像就好


    # @classmethod
    # def create(cls, i,userRAvatar=''):
    #     i = int(i)
    #     userRAlias = get_unique_str(10)
    #     userRPhone = 13713800000+i
    #     userRGender = i%2
    #     return cls(
    #         userRAlias=userRAlias,
    #         userRPhone=str(userRPhone),
    #         userRGender = userRGender,
    #         userRAvatar = userRAvatar,
    #     )
# likeNum commentNum 函数实现就好

# --------------------------------------------------- s ------------------------------
class userS(models.Model):
    userS_Id = models.AutoField(primary_key=True)
    userS_Alias = models.CharField(max_length=20,unique=True)
    userS_Pwd = models.CharField(max_length=20,default='66666666')
    userS_Phone = models.CharField(max_length=12,default='13713800000',unique=True)
    userS_Email = models.EmailField(unique=True)
    userS_Gender = models.BooleanField(default=True)
    userS_Time = models.DateTimeField(default=now())
    # 擅长领域
    userS_Type = models.CharField(max_length=8)
    objects = models.manager.QuerySet

class userLikeS(models.Model):
    userLikeS_Id = models.AutoField(primary_key=True)


    # 关注的人
    userLikeS_User = models.CharField(max_length=6)
    # 关注的人种类
    userLikeS_UserType = models.CharField(max_length=1)

    # 被关注的人的Id
    userLikeS_UserId = models.CharField(max_length=6)
    userLikeS_UserType = models.CharField(max_length=1)
    
    
    userLikeS_Time = models.DateTimeField(default=now())
    
    objects = models.manager.QuerySet

class userCommentS(models.Model):
    userCommentS_Id = models.AutoField(primary_key=True)

    userCommentS_Text = models.CharField(max_length=144,default="还行")
    userCommentS_Star = models.CharField(max_length=1,default='A')

    # 评论人的ID
    userCommentS_ERId = models.CharField(max_length=6)
    userCommentS_ERType = models.CharField(max_length=1)

    # 被评论人的ID
    userCommentS_EEId = models.CharField(max_length=6)
    userCommentS_EEType = models.CharField(max_length=1)

    # 评价人物的时间
    userCommentS_Time = models.DateTimeField(default=now())

    objects = models.manager.QuerySet

# ----------------------------------------- A --------------------------------------

class userA(models.Model):
    userA_Id = models.AutoField(primary_key=True)
    userA_Alias = models.CharField(max_length=20,unique=True)
    userA_Pwd = models.CharField(max_length=20,default='66666666')
    userA_Phone = models.CharField(max_length=12,default='13713800000',unique=True)
    userA_Email = models.EmailField(unique=True)
    userA_Gender = models.BooleanField(default=True)
    userA_Time = models.DateTimeField(default=now())
    # 擅长领域
    userA_Type = models.CharField(max_length=8)
    objects = models.manager.QuerySet

class userLikeA(models.Model):
    userLikeA_Id = models.AutoField(primary_key=True)
    # 关注的人
    userLikeA_User = models.CharField(max_length=6)
    # 关注的人种类
    userLikeA_UserType = models.CharField(max_length=1)

    # 被关注的人的Id
    userLikeA_UserId = models.CharField(max_length=6)
    userLikeA_UserType = models.CharField(max_length=1)
    
    
    userLikeA_Time = models.DateTimeField(default=now())
    objects = models.manager.QuerySet


class userCommentA(models.Model):
    userCommentA_Id = models.AutoField(primary_key=True)

    userCommentA_text = models.CharField(max_length=144,default="还行")
    userCommentA_star = models.CharField(max_length=1,default='A')

    # 评论人的ID
    userCommentA_ERId = models.CharField(max_length=6)
    userCommentA_ERType = models.CharField(max_length=1)

    # 被评论人的ID
    userCommentA_EEId = models.CharField(max_length=6)
    userCommentA_EEType = models.CharField(max_length=1)

    # 评价人物的时间
    userCommentA_Time = models.DateTimeField(default=now())

    objects = models.manager.QuerySet


# ---------------------------------------- B ------------------------------------
    
class userB(models.Model):
    userB_Id = models.AutoField(primary_key=True)
    userB_Blias = models.CharField(max_length=20,unique=True)
    userB_Pwd = models.CharField(max_length=20,default='66666666')
    userB_Phone = models.CharField(max_length=12,default='13713800000',unique=True)
    userB_Email = models.EmailField(unique=True)
    userB_Gender = models.BooleanField(default=True)
    userB_Time = models.DateTimeField(default=now())
    # 擅长领域
    userB_Type = models.CharField(max_length=8)
    objects = models.manager.QuerySet

class userLikeB(models.Model):
    userLikeB_Id = models.AutoField(primary_key=True)


    # 关注的人
    userLikeB_User = models.CharField(max_length=6)
    # 关注的人种类
    userLikeB_UserType = models.CharField(max_length=1)

    # 被关注的人的Id
    userLikeB_UserId = models.CharField(max_length=6)
    userLikeB_UserType = models.CharField(max_length=1)
    
    
    userLikeB_Time = models.DateTimeField(default=now())
    
    objects = models.manager.QuerySet


class userCommentB(models.Model):
    userCommentB_Id = models.AutoField(primary_key=True)

    userCommentB_text = models.CharField(max_length=144,default="还行")
    userCommentB_star = models.CharField(max_length=1,default='B')

    # 评论人的ID
    userCommentB_ERId = models.CharField(max_length=6)
    userCommentB_ERType = models.CharField(max_length=1)

    # 被评论人的ID
    userCommentB_EEId = models.CharField(max_length=6)
    userCommentB_EEType = models.CharField(max_length=1)

    # 评价人物的时间
    userCommentB_Time = models.DateTimeField(default=now())

    objects = models.manager.QuerySet

# ---------------------------------------------- C ---------------------------------
class userC(models.Model):
    userC_Id = models.AutoField(primary_key=True)
    userC_Clias = models.CharField(max_length=20,unique=True)
    userC_Pwd = models.CharField(max_length=20,default='66666666')
    userC_Phone = models.CharField(max_length=12,default='13713800000',unique=True)
    userC_Email = models.EmailField(unique=True)
    userC_Gender = models.BooleanField(default=True)
    userC_Time = models.DateTimeField(default=now())
    # 擅长领域
    userC_Type = models.CharField(max_length=8)
    objects = models.manager.QuerySet

class userLikeC(models.Model):
    userLikeC_Id = models.AutoField(primary_key=True)


    # 关注的人
    userLikeC_User = models.CharField(max_length=6)
    # 关注的人种类
    userLikeC_UserType = models.CharField(max_length=1)

    # 被关注的人的Id
    userLikeC_UserId = models.CharField(max_length=6)
    userLikeC_UserType = models.CharField(max_length=1)
    
    
    userLikeC_Time = models.DateTimeField(default=now())
    
    objects = models.manager.QuerySet


class userCommentC(models.Model):
    userCommentC_Id = models.AutoField(primary_key=True)

    userCommentC_Text = models.CharField(max_length=144,default="还行")
    userCommentC_Star = models.CharField(max_length=1,default='C')

    # 评论人的ID
    userCommentC_ERId = models.CharField(max_length=6)
    userCommentC_ERType = models.CharField(max_length=1)

    # 被评论人的ID
    userCommentC_EEId = models.CharField(max_length=6)
    userCommentC_EEType = models.CharField(max_length=1)

    # 评价人物的时间
    userCommentC_Time = models.DateTimeField(default=now())

    objects = models.manager.QuerySet



# --------------------------------------------------- D E-------------------------------

class userD(models.Model):
    userD_Id = models.AutoField(primary_key=True)
    userD_Alias = models.CharField(max_length=20,unique=True)
    userD_Pwd = models.CharField(max_length=20,default='66666666')
    userD_Phone = models.CharField(max_length=12,default='13713800000',unique=True)
    userD_Email = models.EmailField(unique=True)
    userD_Gender = models.BooleanField(default=True)
    userD_Time = models.DateTimeField(default=now())
    objects = models.manager.QuerySet

class userE(models.Model):
    userE_Id = models.AutoField(primary_key=True)
    userE_Alias = models.CharField(max_length=20,unique=True)
    userE_Pwd = models.CharField(max_length=20,default='66666666')
    userE_Phone = models.CharField(max_length=12,default='13713800000',unique=True)
    userE_Email = models.EmailField(unique=True)
    userE_Gender = models.BooleanField(default=True)
    userE_Time = models.DateTimeField(default=now())
    objects = models.manager.QuerySet


