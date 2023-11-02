from django.db import models
from django.utils.html import format_html


class SkillColor(models.Model):
    skill = models.CharField(max_length=255, unique=True, db_index=True, verbose_name='Навык')
    background = models.CharField(max_length=7, default='#ff6347', verbose_name='Цвет фона')
    color = models.CharField(max_length=7, default='#f5f5f5', verbose_name='Цвет текста')

    class Meta:
        verbose_name = 'Цвет навыка'
        verbose_name_plural = 'Цвета навыков'

    def __str__(self):
        return f'{self.skill}:{self.background} / {self.color}'
