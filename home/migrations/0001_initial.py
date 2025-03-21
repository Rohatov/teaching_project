# Generated by Django 5.0.7 on 2024-09-07 13:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('confg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='confg.basemodel')),
                ('title', models.CharField(max_length=255, verbose_name='sarlavha')),
                ('photo', models.ImageField(upload_to='rasmlar/', verbose_name='Rasm')),
                ('doc', models.FileField(upload_to='documents/', verbose_name='Yutuq')),
            ],
            options={
                'db_table': 'achievements',
            },
            bases=('confg.basemodel',),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='Kategoriya nomi:')),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='confg.basemodel')),
                ('title', models.CharField(max_length=200, verbose_name='Sarlavha')),
                ('photo', models.FileField(upload_to='ish_faoliyati/rasmlar/', verbose_name='Rasm')),
            ],
            options={
                'db_table': 'photos',
            },
            bases=('confg.basemodel',),
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='confg.basemodel')),
                ('title', models.CharField(max_length=200, verbose_name='Sarlavha')),
                ('video', models.FileField(upload_to='ish_faoliyati/videolar/', verbose_name='Video')),
            ],
            options={
                'db_table': 'videos',
            },
            bases=('confg.basemodel',),
        ),
        migrations.CreateModel(
            name='LessonPlans',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='confg.basemodel')),
                ('title', models.CharField(max_length=255, verbose_name='Sarlavha')),
                ('photo', models.ImageField(upload_to='dars-ishlanmalar/rasmlar/', verbose_name='Rasm:')),
                ('desc', models.CharField(max_length=255, verbose_name='Qisqacha malumot:')),
                ('file', models.FileField(upload_to='dars-ishlanmalar/', verbose_name='Dars ishlanma:')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_plan', to='home.category')),
            ],
            options={
                'db_table': 'lesson-plans',
            },
            bases=('confg.basemodel',),
        ),
    ]
