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
    title = models.CharField(max_length=100, verbose_name='вопрос')
    option_1 = models.CharField(max_length=40, verbose_name='вариант 1')
    option_2 = models.CharField(max_length=40, verbose_name='вариант 2')
    option_3 = models.CharField(max_length=40, verbose_name='вариант 3')
    option_4 = models.CharField(max_length=40, verbose_name='вариант 4')
    correct = models.CharField(max_length=3, null=False, default='1', verbose_name='номер правильного ответа(ов)')
    quiz = models.ForeignKey('quiz', null=False, related_name='questions',
                             verbose_name='тест', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']


class Answers(models.Model):
    correct = models.IntegerField(default=0, verbose_name='correct')
    incorrect = models.IntegerField(default=0, verbose_name='incorrect')
