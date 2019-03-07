# _*_ encoding: utf-8 _*_
__author__ = 'nzb'
__date__ = '2019/2/23 12:26'

import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin

from .models import UserProfile, EmailVerifyRecord, Banner

#配置主题功能
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


#全局头部脚步配置
class GlobalSettings(object):
    site_title = '慕课网'
    site_footer = '慕课在线网'
    menu_style = 'accordion'


# class UserProfileAdmin(UserAdmin):
#     def get_form_layout(self):
#         if self.org_obj:
#             self.form_layout = (
                # 显示样式
#                 Main(
#                     Fieldset('',
#                              'username', 'password',
#                              css_class='unsort no_title'
#                              ),
#                     Fieldset(_('Personal info'),
#                              Row('first_name', 'last_name'),
#                              'email'
#                              ),
#                     Fieldset(_('Permissions'),
#                              'groups', 'user_permissions'
#                              ),
#                     Fieldset(_('Important dates'),
#                              'last_login', 'date_joined'
#                              ),
#                 ),
#                 Side(
#                     Fieldset(_('Status'),
#                              'is_active', 'is_staff', 'is_superuser',
#                              ),
#                 )
#             )
#         return super(UserAdmin, self).get_form_layout()


class EmailVerifyRecordAdmin(object):
    # 展示字段
    list_display = ['code', 'email','send_type', 'send_time']
    # 搜索功能
    search_fields = ['code', 'email','send_type']
    # 过滤器
    list_filter = ['code', 'email','send_type', 'send_time']
    # ico图标
    model_icon = 'fa fa-address-book-o'


class BannerAdmin(object):
    list_display = ['title', 'image','url', 'index','add_time']
    search_fields = ['title', 'image','url', 'index']
    list_filter = ['title', 'image','url', 'index','add_time']
    model_icon = 'fa fa-file-image-o'


# xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)