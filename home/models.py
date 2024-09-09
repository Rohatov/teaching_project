from django.db import models
from confg.models import Basemodel
# Create your models here.

class Category(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50, verbose_name='Kategoriya nomi:')

    class Meta:
        ordering = ['-create_at']

    def __str__(self) -> str:
        return self.name
    

class LessonPlans(Basemodel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='lesson_plan')
    title = models.CharField(max_length=255, verbose_name='Sarlavha')
    photo = models.ImageField(upload_to='dars-ishlanmalar/rasmlar/', verbose_name='Rasm:')
    desc = models.CharField(max_length=255, verbose_name='Qisqacha malumot:')
    file = models.FileField(upload_to='dars-ishlanmalar/', verbose_name='Dars ishlanma:')

    class Meta:
        db_table = 'lesson-plans'
        ordering = ['-create_at']
    
    def __str__(self) -> str:
        return self.title


class Achievements(Basemodel):
    title = models.CharField(max_length=255, verbose_name='sarlavha')
    photo = models.ImageField(upload_to='rasmlar/', verbose_name='Rasm')
    doc = models.FileField(upload_to='documents/', verbose_name='Yutuq')

    class Meta:
        db_table = 'achievements'
        ordering = ['-create_at']
    
    def __str__(self) -> str:
        return self.title
    

class Videos(Basemodel):
    title = models.CharField(max_length=200, verbose_name='Sarlavha')
    video = models.FileField(upload_to='ish_faoliyati/videolar/', verbose_name='Video')

    class Meta:
        db_table = 'videos'
        ordering = ['-create_at']

    def __str__(self) -> str:
        return self.title


class Photos(Basemodel):
    title = models.CharField(max_length=200, verbose_name='Sarlavha')
    photo = models.FileField(upload_to='ish_faoliyati/rasmlar/', verbose_name='Rasm')

    class Meta:
        db_table = 'photos'
        ordering = ['-create_at']

    def __str__(self) -> str:
        return self.title
    
