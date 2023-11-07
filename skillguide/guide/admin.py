from django.contrib import admin
from django.utils.html import format_html
from .models import SkillColor, JWTTokens
from .forms import MyModelForm


@admin.register(SkillColor)
class SkillColorAdmin(admin.ModelAdmin):
    form = MyModelForm
    list_display = 'skill', 'display_color'

    def display_color(self, obj):
        return format_html('<div style="background-color: {}; color: {};">{}</div>',
                           obj.background, obj.color, obj.skill)

    display_color.short_description = 'Пример Отображения'


@admin.register(JWTTokens)
class JWTTokensAdmin(admin.ModelAdmin):
    pass
    # form = MyModelForm
    # list_display = 'skill', 'display_color'
    #
    # def display_color(self, obj):
    #     return format_html('<div style="background-color: {}; color: {};">{}</div>',
    #                        obj.background, obj.color, obj.skill)
    #
    # display_color.short_description = 'Пример Отображения'
