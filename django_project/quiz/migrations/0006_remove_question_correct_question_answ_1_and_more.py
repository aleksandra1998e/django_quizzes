# Generated by Django 4.1.3 on 2022-12-05 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_alter_question_correct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='correct',
        ),
        migrations.AddField(
            model_name='question',
            name='answ_1',
            field=models.BooleanField(default=True, verbose_name='Правильно'),
        ),
        migrations.AddField(
            model_name='question',
            name='answ_2',
            field=models.BooleanField(default=False, verbose_name='Правильно'),
        ),
        migrations.AddField(
            model_name='question',
            name='answ_3',
            field=models.BooleanField(default=False, verbose_name='Правильно'),
        ),
        migrations.AddField(
            model_name='question',
            name='answ_4',
            field=models.BooleanField(default=False, verbose_name='Правильно'),
        ),
    ]
