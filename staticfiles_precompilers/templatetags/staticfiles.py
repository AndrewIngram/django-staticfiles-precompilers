import os

from django import template

from django.contrib.staticfiles.templatetags.staticfiles import StaticFilesNode as BaseStaticFilesNode
from django.contrib.staticfiles.storage import staticfiles_storage

from django.conf import settings

register = template.Library()


class StaticFilesNode(BaseStaticFilesNode):

    def url(self, context):
        path = self.path.resolve(context)
        file_name, file_ext = os.path.splitext(path)

        if file_ext in settings.STATICFILES_PRECOMPILERS:
            handler = settings.STATICFILES_PRECOMPILERS[file_ext]
            path = handler[1].format(file_name=file_name)
        return staticfiles_storage.url(path)


@register.tag('static')
def do_static(parser, token):
    return StaticFilesNode.handle_token(parser, token)
