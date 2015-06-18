from django.contrib import admin

from .models import Expression

class ExpressionAdmin(admin.ModelAdmin):
    fieldsets= [
        (None, {'fields': ['expression', 'number']}),
    ]
    list_display = ('number', 'expression')

admin.site.register(Expression, ExpressionAdmin)