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
# ------------------------------------ fsModel.py -----------------------------------
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


# ---------------------------------------QA model.py---------------------------
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


# ----------------------------------------srvModel.py -----------------------------

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

    # 价钱
    srvS_Price= models.CharField(default='0.0',max_length=6)

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


    srvA_Price= models.CharField(default='0.0',max_length=6)
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

    srvC_Price= models.CharField(default='0.0',max_length=6)
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


# -------------------------------userModel.py------------------------------------
# ---------------------------------user 用户 RSABC-------------------------------------

class userR(models.Model):
    userR_Id = models.AutoField(primary_key=True)
    userR_Alias = models.CharField(max_length=20,unique=True)
    userR_Pwd = models.CharField(max_length=20,default='66666666')
    userR_Phone = models.CharField(max_length=12,default='13713800000',unique=True)
    userR_Email = models.EmailField(unique=True)
    userR_Gender = models.BooleanField(default=True)

    userR_Time = models.DateTimeField(default=now())

    # 普通用户可作为标签 服务提供者可作为资历说明
    userR_Label = models.CharField(blank=True,max_length=40)
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

    userS_Label = models.CharField(blank=True, max_length=40)
    # 擅长领域
    userS_Type = models.CharField(max_length=8)
    objects = models.manager.QuerySet

class userLikeS(models.Model):
    userLikeS_Id = models.AutoField(primary_key=True)


    # 关注的人
    userLikeS_ERId = models.CharField(max_length=6)
    # 关注的人种类
    userLikeS_ERType = models.CharField(max_length=1)

    # 被关注的人的Id
    userLikeS_EEId = models.CharField(max_length=6)
    userLikeS_EEType = models.CharField(max_length=1)
    
    
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

    userA_Label = models.CharField(blank=True, max_length=40)
    # 擅长领域
    userA_Type = models.CharField(max_length=8)
    objects = models.manager.QuerySet

class userLikeA(models.Model):
    userLikeA_Id = models.AutoField(primary_key=True)
    # 关注的人
    userLikeA_ER = models.CharField(max_length=6)
    # 关注的人种类
    userLikeA_ERType = models.CharField(max_length=1)

    # 被关注的人的Id
    userLikeA_EEId = models.CharField(max_length=6)
    userLikeA_EEType = models.CharField(max_length=1)
    
    
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

    userB_Label = models.CharField(blank=True, max_length=40)
    # 擅长领域
    userB_Type = models.CharField(max_length=8)
    objects = models.manager.QuerySet

class userLikeB(models.Model):
    userLikeB_Id = models.AutoField(primary_key=True)


    # 关注的人
    userLikeB_ER = models.CharField(max_length=6)
    # 关注的人种类
    userLikeB_ERType = models.CharField(max_length=1)

    # 被关注的人的Id
    userLikeB_EEId = models.CharField(max_length=6)
    userLikeB_EEType = models.CharField(max_length=1)
    
    
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


    userC_Label = models.CharField(blank=True, max_length=40)

    # 擅长领域
    userC_Type = models.CharField(max_length=8)
    objects = models.manager.QuerySet

class userLikeC(models.Model):
    userLikeC_Id = models.AutoField(primary_key=True)


    # 关注的人
    userLikeC_ER = models.CharField(max_length=6)
    # 关注的人种类
    userLikeC_ERType = models.CharField(max_length=1)

    # 被关注的人的Id
    userLikeC_EEId = models.CharField(max_length=6)
    userLikeC_EEType = models.CharField(max_length=1)
    
    
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

    userD_Label = models.CharField(blank=True, max_length=40)
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


