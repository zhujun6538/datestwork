from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig

class ApitestConfig(AppConfig):
    name = 'apitest'
    verbose_name = 'api测试'


class MyAdminConfig(AdminConfig):
    default_site = 'apitest.admin.EventAdminSite'