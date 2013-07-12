# -*- coding: utf-8 -*-
#
# Copyright (©) 2013 Gustavo Noronha Silva <gustavo@noronha.eti.br>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

import locale
from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter
def format_currency(value):
    return mark_safe(locale.currency(value, grouping=True).replace(" ", "&nbsp;"))


@register.filter
def itercycle(iterable, counter):
    return iterable[counter % len(iterable)]