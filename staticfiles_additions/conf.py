from django.conf import settings
from appconf import AppConf


class StaticFilesAdditionsConf(AppConf):
    PRECOMPILERS = {
        '.scss': ('scss {infile} {outfile}', '{file_name}.css'),
        '.handlebars': ('handlebars {infile} -f {outfile}', '{file_name}.handlebars.js'),
    }

    class Meta:
        prefix = 'staticfiles'