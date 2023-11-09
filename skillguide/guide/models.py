from django.db import models
from django.contrib.auth.models import User


class JWTTokens(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=255)
    api_id = models.IntegerField()


class SkillColor(models.Model):
    skill = models.CharField(max_length=255, unique=True, db_index=True, verbose_name='Навык')
    background = models.CharField(max_length=7, default='#ff6347', verbose_name='Цвет фона')
    color = models.CharField(max_length=7, default='#f5f5f5', verbose_name='Цвет текста')

    class Meta:
        verbose_name = 'Цвет навыка'
        verbose_name_plural = 'Цвета навыков'

    def __str__(self):
        return f'{self.skill}:{self.background} / {self.color}'


class UploadAPIImages(models.Model):
    image = models.ImageField(upload_to='api/%Y/%m/%d/', verbose_name='Изображение')
    type_image = models.CharField(max_length=30, unique=True, db_index=True, verbose_name='Тип файла')

    class Meta:
        verbose_name = 'API изображение'
        verbose_name_plural = 'API изображения'
