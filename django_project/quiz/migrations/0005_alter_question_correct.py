# Generated by Django 4.1.3 on 2022-12-05 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_answers_alter_question_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct',
            field=models.CharField(choices=[('1', ''), ('2', ''), ('3', ''), ('4', '')], default='1', max_length=3, verbose_name='номер правильного ответа(ов)'),
        ),
    ]
