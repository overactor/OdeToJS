"""
    Admin settings for OdeToJS
    Copyright (C) 2015  Rik de Graaff

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

from django.contrib import admin

from .models import Expression

class ExpressionAdmin(admin.ModelAdmin):
    fieldsets= [
        (None, {'fields': ['expression', 'number']}),
    ]
    list_display = ('number', 'expression')

admin.site.register(Expression, ExpressionAdmin)