class userC(models.Model):
    userC_Id = models.AutoField(primary_key=True)
    userC_Clias = models.CharField(max_length=20,unique=True)
    userC_Pwd = models.CharField(max_length=20,default='66666666')
    userC_Phone = models.CharField(max_length=12,default='13713800000',unique=True)
    userC_Email = models.EmailField(unique=True)
    userC_Gender = models.CooleanField(default=True)
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

    userCommentC_text = models.CharField(max_length=144,default="还行")
    userCommentC_star = models.CharField(max_length=1,default='C')

    # 评论人的ID
    userCommentC_ERId = models.CharField(max_length=6)
    userCommentC_ERType = models.CharField(max_length=1)

    # 被评论人的ID
    userCommentC_EEId = models.CharField(max_length=6)
    userCommentC_EEType = models.CharField(max_length=1)

    # 评价人物的时间
    userCommentC_Time = models.DateTimeField(default=now())

    objects = models.manager.QuerySet