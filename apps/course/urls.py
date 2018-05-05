# -*- coding:utf-8 -*- 
#!/usr/bin/env python
# @Author  : tianbao
# @Contact : gmu1592618@gmail.com
# @Time    : 2018/4/30 9:09
# @File    : urls.py
# @Software: PyCharm
from django.urls import path,re_path
from .views import CourseListView,CourseDetailView,CourseInfoView,CommentsView,AddCommentsView
from .views import VideoPlayView


# 要写上app的名字
app_name = "course"

urlpatterns = [
    path('list/',CourseListView.as_view(),name='course_list'),
    re_path('course/(?P<course_id>\d+)/', CourseDetailView.as_view(), name="course_detail"),
    re_path('info/(?P<course_id>\d+)/', CourseInfoView.as_view(), name="course_info"),
    re_path('comment/(?P<course_id>\d+)/', CommentsView.as_view(), name="course_comments"),
    path('add_comment/', AddCommentsView.as_view(), name="add_comment"),
    path('video/(?P<video_id>\d+)/', VideoPlayView.as_view(), name="video_play"),


]