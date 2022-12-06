from django.core.exceptions import ValidationError
from django.db import models


class Quiz(models.Model):
    name = models.CharField(unique=True, null=False, max_length=50, verbose_name='название теста')
    description = models.CharField(null=False, max_length=500, default='Удачи', verbose_name='описание')
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='дата добавления')
    date_edit = models.DateTimeField(auto_now=True, verbose_name='дата изменения')

    class Meta:
        ordering = ['date_add']

    def __str__(self):
        return self.name


class Question(models.Model):
    STATUS_CHOICES = [('1', ''), ('2', ''), ('3', ''), ('4', '')]
    title = models.CharField(max_length=100, verbose_name='вопрос')
    option_1 = models.CharField(max_length=40, verbose_name='вариант 1')
    answ_1 = models.BooleanField(verbose_name='Правильно', default=True)
    option_2 = models.CharField(max_length=40, verbose_name='вариант 2')
    answ_2 = models.BooleanField(verbose_name='Правильно', default=False)
    option_3 = models.CharField(max_length=40, verbose_name='вариант 3')
    answ_3 = models.BooleanField(verbose_name='Правильно', default=False)
    option_4 = models.CharField(max_length=40, verbose_name='вариант 4')
    answ_4 = models.BooleanField(verbose_name='Правильно', default=False)
    quiz = models.ForeignKey('quiz', null=False, related_name='questions',
                             verbose_name='тест', on_delete=models.CASCADE)
    correct = models.CharField(max_length=6, default='')

    def clean(self):
        if self.answ_1 and self.answ_2 and self.answ_3 and self.answ_4:
            raise ValidationError('Максимум 3 правильных ответа')
        elif not self.answ_1 and not self.answ_2 and not self.answ_3 and not self.answ_4:
            raise ValidationError('Минимум 1 правильный ответ')

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        answ = ''
        if self.answ_1:
            answ += '1 '
        if self.answ_2:
            answ += '2 '
        if self.answ_3:
            answ += '3 '
        if self.answ_4:
            answ += '4 '
        self.correct = answ[:-1]
        super().save()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']


class Answers(models.Model):
    correct = models.IntegerField(default=0, verbose_name='correct')
    incorrect = models.IntegerField(default=0, verbose_name='incorrect')
