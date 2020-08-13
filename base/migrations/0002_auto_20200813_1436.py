# Generated by Django 3.0.2 on 2020-08-13 14:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='srvcommenta',
            name='srvCommentA_SrvType',
        ),
        migrations.RemoveField(
            model_name='srvcommentc',
            name='srvCommentC_SrvType',
        ),
        migrations.RemoveField(
            model_name='srvcomments',
            name='srvCommentS_Srv',
        ),
        migrations.RemoveField(
            model_name='srvcomments',
            name='srvCommentS_SrvType',
        ),
        migrations.RemoveField(
            model_name='srvcomments',
            name='srvCommentS_User',
        ),
        migrations.RemoveField(
            model_name='srvlikec',
            name='srvLikeC_User',
        ),
        migrations.RemoveField(
            model_name='srvusera',
            name='srvUserA_SrvType',
        ),
        migrations.RemoveField(
            model_name='srvuserc',
            name='srvUserC_SrvType',
        ),
        migrations.RemoveField(
            model_name='usercommenta',
            name='userCommentA_ERType',
        ),
        migrations.RemoveField(
            model_name='usercommentb',
            name='userCommentB_EEType',
        ),
        migrations.RemoveField(
            model_name='usercommentc',
            name='userCommentC_EEType',
        ),
        migrations.RemoveField(
            model_name='usercomments',
            name='userCommentS_EEType',
        ),
        migrations.RemoveField(
            model_name='userlikea',
            name='userLikeA_User',
        ),
        migrations.RemoveField(
            model_name='userlikea',
            name='userLikeA_UserId',
        ),
        migrations.RemoveField(
            model_name='userlikea',
            name='userLikeA_UserType',
        ),
        migrations.RemoveField(
            model_name='userlikeb',
            name='userLikeB_User',
        ),
        migrations.RemoveField(
            model_name='userlikeb',
            name='userLikeB_UserId',
        ),
        migrations.RemoveField(
            model_name='userlikeb',
            name='userLikeB_UserType',
        ),
        migrations.RemoveField(
            model_name='userlikec',
            name='userLikeC_User',
        ),
        migrations.RemoveField(
            model_name='userlikec',
            name='userLikeC_UserId',
        ),
        migrations.RemoveField(
            model_name='userlikec',
            name='userLikeC_UserType',
        ),
        migrations.RemoveField(
            model_name='userlikes',
            name='userLikeS_User',
        ),
        migrations.RemoveField(
            model_name='userlikes',
            name='userLikeS_UserId',
        ),
        migrations.RemoveField(
            model_name='userlikes',
            name='userLikeS_UserType',
        ),
        migrations.AddField(
            model_name='srva',
            name='srvA_Price',
            field=models.CharField(default='0.0', max_length=6),
        ),
        migrations.AddField(
            model_name='srvc',
            name='srvC_Price',
            field=models.CharField(default='0.0', max_length=6),
        ),
        migrations.AddField(
            model_name='srvcomments',
            name='srvCommentS_SrvId',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AddField(
            model_name='srvcomments',
            name='srvCommentS_UserId',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AddField(
            model_name='srvlikec',
            name='srvLikeC_UserId',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AddField(
            model_name='srvs',
            name='srvS_Price',
            field=models.CharField(default='0.0', max_length=6),
        ),
        migrations.AddField(
            model_name='usera',
            name='userA_Label',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='userb',
            name='userB_Label',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='userc',
            name='userC_Label',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='userd',
            name='userD_Label',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='userlikea',
            name='userLikeA_EEId',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AddField(
            model_name='userlikea',
            name='userLikeA_ER',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AddField(
            model_name='userlikea',
            name='userLikeA_ERType',
            field=models.CharField(default='D', max_length=6),
        ),
        migrations.AddField(
            model_name='userlikeb',
            name='userLikeB_EEId',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AddField(
            model_name='userlikeb',
            name='userLikeB_ER',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AddField(
            model_name='userlikeb',
            name='userLikeB_ERType',
            field=models.CharField(default='0', max_length=1),
        ),
        migrations.AddField(
            model_name='userlikec',
            name='userLikeC_EEId',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AddField(
            model_name='userlikec',
            name='userLikeC_ER',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AddField(
            model_name='userlikec',
            name='userLikeC_ERType',
            field=models.CharField(default='0', max_length=1),
        ),
        migrations.AddField(
            model_name='userlikes',
            name='userLikeS_EEId',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AddField(
            model_name='userlikes',
            name='userLikeS_ERId',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AddField(
            model_name='userlikes',
            name='userLikeS_ERType',
            field=models.CharField(default='D', max_length=6),
        ),
        migrations.AddField(
            model_name='userr',
            name='userR_Label',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='users',
            name='userS_Label',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='ans',
            name='ans_QuesId',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='ans',
            name='ans_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 260551)),
        ),
        migrations.AlterField(
            model_name='ans',
            name='ans_User',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='ans',
            name='ans_UserType',
            field=models.CharField(default='D', max_length=6),
        ),
        migrations.AlterField(
            model_name='anslike',
            name='ansLike_AnsId',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='anslike',
            name='ansLike_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 260551)),
        ),
        migrations.AlterField(
            model_name='anslike',
            name='ansLike_User',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='anslike',
            name='ansLike_UserType',
            field=models.CharField(default='D', max_length=6),
        ),
        migrations.AlterField(
            model_name='fs',
            name='fs_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 258497)),
        ),
        migrations.AlterField(
            model_name='fs',
            name='fs_User',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='fs',
            name='fs_UserType',
            field=models.CharField(default='D', max_length=6),
        ),
        migrations.AlterField(
            model_name='fscomment',
            name='fsComment_Srv',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='fscomment',
            name='fsComment_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 258497)),
        ),
        migrations.AlterField(
            model_name='fscomment',
            name='fsComment_User',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='fscomment',
            name='fsComment_UserType',
            field=models.CharField(default='D', max_length=6),
        ),
        migrations.AlterField(
            model_name='fslike',
            name='fsLike_AnsId',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='fslike',
            name='fsLike_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 259553)),
        ),
        migrations.AlterField(
            model_name='fslike',
            name='fsLike_User',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='fslike',
            name='fsLike_UserType',
            field=models.CharField(default='D', max_length=6),
        ),
        migrations.AlterField(
            model_name='ques',
            name='ques_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 259553)),
        ),
        migrations.AlterField(
            model_name='ques',
            name='ques_User',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='ques',
            name='ques_UserType',
            field=models.CharField(default='D', max_length=6),
        ),
        migrations.AlterField(
            model_name='queslike',
            name='quesLike_AnsId',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='queslike',
            name='quesLike_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 259553)),
        ),
        migrations.AlterField(
            model_name='queslike',
            name='quesLike_User',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='queslike',
            name='quesLike_UserType',
            field=models.CharField(default='D', max_length=6),
        ),
        migrations.AlterField(
            model_name='srva',
            name='srvA_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 262547)),
        ),
        migrations.AlterField(
            model_name='srvc',
            name='srvC_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 263547)),
        ),
        migrations.AlterField(
            model_name='srvcommenta',
            name='srvCommentA_Srv',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='srvcommenta',
            name='srvCommentA_Star',
            field=models.CharField(default='D', max_length=6),
        ),
        migrations.AlterField(
            model_name='srvcommenta',
            name='srvCommentA_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 262547)),
        ),
        migrations.AlterField(
            model_name='srvcommenta',
            name='srvCommentA_User',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='srvcommenta',
            name='srvCommentA_UserType',
            field=models.CharField(default='D', max_length=6),
        ),
        migrations.AlterField(
            model_name='srvcommentc',
            name='srvCommentC_Srv',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='srvcommentc',
            name='srvCommentC_Star',
            field=models.CharField(default='D', max_length=6),
        ),
        migrations.AlterField(
            model_name='srvcommentc',
            name='srvCommentC_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 263547)),
        ),
        migrations.AlterField(
            model_name='srvcommentc',
            name='srvCommentC_User',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='srvcommentc',
            name='srvCommentC_UserType',
            field=models.CharField(default='D', max_length=6),
        ),
        migrations.AlterField(
            model_name='srvcomments',
            name='srvCommentS_Star',
            field=models.CharField(default='D', max_length=6),
        ),
        migrations.AlterField(
            model_name='srvcomments',
            name='srvCommentS_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 260551)),
        ),
        migrations.AlterField(
            model_name='srvcomments',
            name='srvCommentS_UserType',
            field=models.CharField(default='D', max_length=1),
        ),
        migrations.AlterField(
            model_name='srvlikea',
            name='srvLikeA_AnsId',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='srvlikea',
            name='srvLikeA_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 262547)),
        ),
        migrations.AlterField(
            model_name='srvlikea',
            name='srvLikeA_User',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='srvlikea',
            name='srvLikeA_UserType',
            field=models.CharField(default='D', max_length=6),
        ),
        migrations.AlterField(
            model_name='srvlikec',
            name='srvLikeC_CnsId',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='srvlikec',
            name='srvLikeC_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 271498)),
        ),
        migrations.AlterField(
            model_name='srvlikec',
            name='srvLikeC_UserType',
            field=models.CharField(default='D', max_length=6),
        ),
        migrations.AlterField(
            model_name='srvlikes',
            name='srvLikeS_AnsId',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='srvlikes',
            name='srvLikeS_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 261548)),
        ),
        migrations.AlterField(
            model_name='srvlikes',
            name='srvLikeS_User',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='srvlikes',
            name='srvLikeS_UserType',
            field=models.CharField(default='D', max_length=6),
        ),
        migrations.AlterField(
            model_name='srvs',
            name='srvS_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 260551)),
        ),
        migrations.AlterField(
            model_name='srvusera',
            name='srvUserA_Id',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='srvusera',
            name='srvUserA_SrvId',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='srvusera',
            name='srvUserA_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 263547)),
        ),
        migrations.AlterField(
            model_name='srvusera',
            name='srvUserA_Type',
            field=models.CharField(default='D', max_length=6),
        ),
        migrations.AlterField(
            model_name='srvuserc',
            name='srvUserC_Id',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='srvuserc',
            name='srvUserC_SrvId',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='srvuserc',
            name='srvUserC_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 271498)),
        ),
        migrations.AlterField(
            model_name='srvuserc',
            name='srvUserC_Type',
            field=models.CharField(default='D', max_length=6),
        ),
        migrations.AlterField(
            model_name='srvusers',
            name='srvUserS_Id',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='srvusers',
            name='srvUserS_SrvId',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='srvusers',
            name='srvUserS_SrvType',
            field=models.CharField(default='D', max_length=6),
        ),
        migrations.AlterField(
            model_name='srvusers',
            name='srvUserS_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 261548)),
        ),
        migrations.AlterField(
            model_name='srvusers',
            name='srvUserS_Type',
            field=models.CharField(default='D', max_length=6),
        ),
        migrations.AlterField(
            model_name='usera',
            name='userA_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 272460)),
        ),
        migrations.AlterField(
            model_name='userb',
            name='userB_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 273492)),
        ),
        migrations.AlterField(
            model_name='userc',
            name='userC_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 274514)),
        ),
        migrations.AlterField(
            model_name='usercommenta',
            name='userCommentA_EEId',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='usercommenta',
            name='userCommentA_EEType',
            field=models.CharField(default='D', max_length=6),
        ),
        migrations.AlterField(
            model_name='usercommenta',
            name='userCommentA_ERId',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='usercommenta',
            name='userCommentA_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 273492)),
        ),
        migrations.AlterField(
            model_name='usercommentb',
            name='userCommentB_EEId',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='usercommentb',
            name='userCommentB_ERId',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='usercommentb',
            name='userCommentB_ERType',
            field=models.CharField(default='0', max_length=1),
        ),
        migrations.AlterField(
            model_name='usercommentb',
            name='userCommentB_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 274514)),
        ),
        migrations.AlterField(
            model_name='usercommentc',
            name='userCommentC_EEId',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='usercommentc',
            name='userCommentC_ERId',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='usercommentc',
            name='userCommentC_ERType',
            field=models.CharField(default='D', max_length=1),
        ),
        migrations.AlterField(
            model_name='usercommentc',
            name='userCommentC_Star',
            field=models.CharField(default='A', max_length=1),
        ),
        migrations.AlterField(
            model_name='usercommentc',
            name='userCommentC_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 275511)),
        ),
        migrations.AlterField(
            model_name='usercomments',
            name='userCommentS_EEId',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='usercomments',
            name='userCommentS_ERId',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AlterField(
            model_name='usercomments',
            name='userCommentS_ERType',
            field=models.CharField(default='D', max_length=6),
        ),
        migrations.AlterField(
            model_name='usercomments',
            name='userCommentS_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 272460)),
        ),
        migrations.AlterField(
            model_name='userd',
            name='userD_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 275511)),
        ),
        migrations.AlterField(
            model_name='usere',
            name='userE_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 275511)),
        ),
        migrations.AlterField(
            model_name='userlikea',
            name='userLikeA_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 273492)),
        ),
        migrations.AlterField(
            model_name='userlikeb',
            name='userLikeB_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 274514)),
        ),
        migrations.AlterField(
            model_name='userlikec',
            name='userLikeC_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 274514)),
        ),
        migrations.AlterField(
            model_name='userlikes',
            name='userLikeS_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 272460)),
        ),
        migrations.AlterField(
            model_name='userr',
            name='userR_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 271498)),
        ),
        migrations.AlterField(
            model_name='users',
            name='userS_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 14, 36, 27, 271498)),
        ),
    ]
