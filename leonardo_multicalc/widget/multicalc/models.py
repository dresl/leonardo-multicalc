# -#- coding: utf-8 -#-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from leonardo.module.web.models import Widget
from leonardo.module.web.models import Page

class MultiCalculatorWidget(Widget):

    color = models.CharField(verbose_name=_("Color"), max_length=255, blank=True)

    class Meta:
        abstract = True
        verbose_name = _('Multi Calc')
        verbose_name_plural = _('Multi Calcs')