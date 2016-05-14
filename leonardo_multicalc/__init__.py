
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

default_app_config = 'leonardo_multicalc.Config'

class Default(object):

    optgroup = 'Calculator'

    apps = [
        'leonardo_multicalc'
    ]

    css_files = [
    	'multicalc/default.css'
    ]

    widgets = [
        'leonardo_multicalc.widget.multicalc.models.MultiCalculatorWidget'
    ]


class Config(AppConfig, Default):
    name = 'leonardo_multicalc'
    verbose_name = _("IconLink")

default = Default()
