import os
import sys

from django.apps import AppConfig


class FeeConfig(AppConfig):
    if os.environ.get('RUN_MAIN', None) != 'true':
        default_app_config = 'mydjangoapp.apps.MydjangoappConfig'
    name = 'fee'

    def ready(self):
        if 'runserver' in sys.argv:
            from .models.impose_type import ImposeType
            default_impose_types = ['세대별부과', '세대구성원별부과']
            for default in default_impose_types:
                if not ImposeType.objects.filter(name=default).exists():
                    ImposeType(name=default, description=default).save()

