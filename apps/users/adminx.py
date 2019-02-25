# _*_ encoding: utf-8 _*_
__author__ = 'nzb'
__date__ = '2019/2/23 12:26'

import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner

#配置主题功能
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


#全局头部脚步配置
class GlobalSettings(object):
    site_title = '慕课网'
    site_footer = '慕课在线网'
    menu_style = 'accordion'



class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email','send_type', 'send_time']
    search_fields = ['code', 'email','send_type']
    list_filter = ['code', 'email','send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image','url', 'index','add_time']
    search_fields = ['title', 'image','url', 'index']
    list_filter = ['title', 'image','url', 'index','add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)