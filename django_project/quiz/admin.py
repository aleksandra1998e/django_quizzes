from django.contrib import admin
from .models import Quiz, Question


class QuestionInLine(admin.StackedInline):
    model = Question
    exclude = ['correct']


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_add']
    search_fields = ['name']
    inlines = [QuestionInLine]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'quiz']
    list_filter = ['quiz']
    search_fields = ['title']
    exclude = ['correct']
