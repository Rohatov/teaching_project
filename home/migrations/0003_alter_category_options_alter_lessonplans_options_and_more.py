# Generated by Django 5.0.7 on 2024-09-07 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_achievements_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-create_at']},
        ),
        migrations.AlterModelOptions(
            name='lessonplans',
            options={'ordering': ['-create_at']},
        ),
        migrations.AlterModelOptions(
            name='photos',
            options={'ordering': ['-create_at']},
        ),
        migrations.AlterModelOptions(
            name='videos',
            options={'ordering': ['-create_at']},
        ),
    ]
