# 慕课网

#### 1、使用指导
    1.1、pip install -r requirements.txt安装依赖包,xadmin需要下载源码包自定义安装。
    
    1.2、安装完后需要替换xadmin的图标样式，找到xadmin位置下的\static\xadmin\vendor\font-awesome\,该目录下有两个文件，百度搜索font-awesome后进入官网下载最新版本，解压后替换css和fonts文件夹
    
    1.3、后台xadmin样式，找到xadmin目录下的static目录下的xadmin，然后拷贝到项目目录下的static目录
#### 2、全局配置
##### 2.1、send_mail配置
    EMAIL_HOST = "smtp.sina.cn"
    EMAIL_PORT = 25
    EMAIL_HOST_USER = "username@sina.cn"
    EMAIL_HOST_PASSWORD = "password"
    EMAIL_USER_TLS = False
    EMAIL_FROM = "username@sina.cn"
##### 2.2、数据库配置
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  #数据库类型
        'NAME': 'dbname',
        'USER':'username',
        'PASSWORD': 'password',
        'HOST': 'hostname',
        }
    }
#### 3、插件使用
##### 3.1、富文本插件
###### 3.1.1、安装方法
    * 方法一：将github整个源码包下载回家，在命令行运行(推荐，兼容py3)：
        下载地址：https://github.com/andyzsf/DjangoUeditor3
        python setup.py install
    * 方法二：使用pip工具在命令行运行(pip安装的版本不兼容py3)：
        pip install DjangoUeditor
###### 3.1.2、使用方法
    具体配置按照：https://github.com/andyzsf/DjangoUeditor3
    简述如下：
    1、安装完后在INSTALL_APPS里面增加DjangoUeditor，如下： INSTALLED_APPS = ( #........ 'DjangoUeditor', ) 
    2、配置urls path('ueditor/',include('DjangoUeditor.urls' )),
    3、xadmin下的plugins中添加ueditor.py文件，在__init__中加入ueditor
    4、最后在需要富文本编辑器插件的app下的adminx文件中添加style_fields={"模型的某个字段":"ueditor"}
    5、ueditor.py文件：
    
            # _*_encoding: utf-8 _*_
            import xadmin
            from xadmin.views import BaseAdminPlugin, CreateAdminView, ModelFormAdminView, UpdateAdminView
            from DjangoUeditor.models import UEditorField
            from DjangoUeditor.widgets import UEditorWidget
            from django.conf import settings
            
            
            class XadminUEditorWidget(UEditorWidget):
                def __init__(self,**kwargs):
                    self.ueditor_options=kwargs
                    self.Media.js = None
                    super(XadminUEditorWidget,self).__init__(kwargs)
            
            class UeditorPlugin(BaseAdminPlugin):
            
                def get_field_style(self, attrs, db_field, style, **kwargs):
                    if style == 'ueditor':
                        if isinstance(db_field, UEditorField):
                            widget = db_field.formfield().widget
                            param = {}
                            param.update(widget.ueditor_settings)
                            param.update(widget.attrs)
                            return {'widget': XadminUEditorWidget(**param)}
                    return attrs
            
                def block_extrahead(self, context, nodes):
                    js = '<script type="text/javascript" src="%s"></script>' % (settings.STATIC_URL + "ueditor/ueditor.config.js")         #自己的静态目录
                    js += '<script type="text/javascript" src="%s"></script>' % (settings.STATIC_URL + "ueditor/ueditor.all.min.js")   #自己的静态目录
                    nodes.append(js)
            
            xadmin.site.register_plugin(UeditorPlugin, UpdateAdminView)
            xadmin.site.register_plugin(UeditorPlugin, CreateAdminView)``