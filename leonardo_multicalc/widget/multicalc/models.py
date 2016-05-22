# -#- coding: utf-8 -#-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from leonardo.module.web.models import Widget
from leonardo.module.web.models import Page

class MultiCalculatorWidget(Widget):

    colorth = models.CharField(verbose_name=_("Color of table head"), max_length=255, blank=True)
    colorthActive = models.CharField(verbose_name=_("Color of active table head"), max_length=255, blank=True)

    class Meta:
        abstract = True
        verbose_name = _('Multi Calc')
        verbose_name_plural = _('Multi Calcs')