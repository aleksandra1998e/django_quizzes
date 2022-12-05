# Generated by Django 4.1.3 on 2022-12-04 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_question_correct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='count',
        ),
        migrations.AddField(
            model_name='quiz',
            name='description',
            field=models.CharField(default='Удачи', max_length=500, verbose_name='описание'),
        ),
    ]
