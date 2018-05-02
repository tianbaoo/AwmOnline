# 博客园
[个人博客园](http://www.cnblogs.com/guotianbao/)  
# Windows7下安装运行  
把AwmOnline文件下载下来  
1. 打开cmd窗口输入：pip install virtualenv 创建虚拟环境（前提是你已经安装好pip）  
2. 桌面新建一个名为Test的文件夹,进入该文件夹Shift+鼠标右键打开cmd输入：virtualenv testenv  
3. Test的文件夹内生成了testenv文件夹，进入testenv文件夹的Scripts文件夹中，Shift+鼠标右键打开cmd输入：activate激活虚拟环境  
4. 把下载的AwmOnline文件夹拖入Scripts文件夹中，在cmd中进入AwmOnline文件夹：cd AwmOnline  
5. requirements.txt所在AwmOnline文件夹内，在cmd输入：pip install -r requirements.txt 回车    
6. 安装完所有的环境依赖后，在cmd中再输入：python manage.py runserver  
7. 不要关闭cmd窗口，去浏览器打开：127.0.0.1:8000 看看是否可以访问。  
# 功能
1. 系统具有完整的用户登录注册以及找回密码功能，拥有完整个人中心。
2. 个人中心: 修改头像，修改密码，修改邮箱，可以看到我的课程以及我的收藏。可以删除收藏，我的消息。
3. 导航栏: 公开课，授课讲师，授课机构，全局搜索。
4. 点击公开课–> 课程列表，排序-搜索。热门课程推荐，课程的分页。
5. 点击课程–> 课程详情页中对课程进行收藏，取消收藏。富文本展示课程内容。
6. 点击开始学习–> 课程的章节信息，课程的评论信息。课程资源的下载链接。
7. 点击授课讲师–>授课讲师列表页，对讲师进行人气排序以及分页，右边有讲师排行榜。
8. 点击讲师的详情页面–> 对讲师进行收藏和分享，以及讲师的全部课程。
9. 导航栏: 授课机构有分页，排序筛选功能。
10. 机构列表页右侧有快速提交我要学习的表单。
11. 点击机构–> 左侧：机构首页,机构课程，机构介绍，机构讲师。
12. 后台管理系统可以切换主题。左侧每一个功能都有列表显示, 增删改查，筛选功能。
13. 课程列表页可以对不同字段进行排序。选择多条记录进行删除操作。
14. 课程列表页：过滤器->选择字段范围等,搜索,导出csv，xml，json。
15. 课程新增页面上传图片，富文本的编辑。时间选择，添加章节，添加课程资源。
16. 日志记录：记录后台人员的操作
# 预览
### 首页
![image](https://raw.githubusercontent.com/tianbaoo/AwmOnline/master/pic_image/%E9%A6%96%E9%A1%B5.png)  
### 公开课
![image](https://raw.githubusercontent.com/tianbaoo/AwmOnline/master/pic_image/%E5%85%AC%E5%BC%80%E8%AF%BE.png)  
### 机构
![image](https://raw.githubusercontent.com/tianbaoo/AwmOnline/master/pic_image/%E6%9C%BA%E6%9E%84%E9%A1%B5.png)  
### 教师
![image](https://raw.githubusercontent.com/tianbaoo/AwmOnline/master/pic_image/%E6%95%99%E5%B8%88%E9%A1%B5.png)  
### 登录
![image](https://raw.githubusercontent.com/tianbaoo/AwmOnline/master/pic_image/%E7%99%BB%E5%BD%95.png)  
### 注册
![image](https://raw.githubusercontent.com/tianbaoo/AwmOnline/master/pic_image/%E6%B3%A8%E5%86%8C%E9%A1%B5.png)  
### 个人中心
![image](https://raw.githubusercontent.com/tianbaoo/AwmOnline/master/pic_image/%E4%B8%AA%E4%BA%BA%E4%B8%AD%E5%BF%83.png)  
### xadmin后台管理
![image](https://raw.githubusercontent.com/tianbaoo/AwmOnline/master/pic_image/%E5%90%8E%E5%8F%B0xadmin.png)  

















