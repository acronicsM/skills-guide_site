from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import SkillColor, JWTTokens, UploadAPIImages
from .forms import MyModelForm


@admin.register(SkillColor)
class SkillColorAdmin(admin.ModelAdmin):
    form = MyModelForm
    list_display = 'skill', 'display_color'

    def display_color(self, obj):
        return format_html('<div style="background-color: {}; color: {};">{}</div>',
                           obj.background, obj.color, obj.skill)

    display_color.short_description = 'Пример Отображения'


@admin.register(UploadAPIImages)
class UploadAPIImagesAdmin(admin.ModelAdmin):
    fields = ['image', 'post_image']
    readonly_fields = ['post_image']
    list_display = 'id', 'image', 'post_image'

    @admin.display(description='Изображение')
    def post_image(self, image: UploadAPIImages):
        return mark_safe(f'<img src="{image.image.url}" width=50>')


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
