from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic, View

from .models import Quiz, Question, Answers


class QuizListView(generic.ListView):
    model = Quiz
    template_name = 'quiz_list.html'
    context_object_name = 'quiz_list'


class QuizDetailView(generic.DetailView):
    model = Quiz
    template_name = 'quiz_detail.html'


class QuizQuestion1View(View):

    def get(self, request, quiz_id):

        quiz = Quiz.objects.get(id=quiz_id)
        questions = Question.objects.filter(quiz=quiz)
        count = Question.objects.filter(quiz=quiz).count()
        answ = Answers()
        answ.save()
        idenef = answ.id
        question = questions[0]
        number = 1
        return render(request, 'question.html', context={
            'question': question, 'number': number, 'quiz_id': quiz_id,
            'quiz': quiz, 'count': count, 'idenef': idenef
        })


class QuizQuestionView(View):

    def get(self, request, quiz_id, number, idenef):

        quiz = Quiz.objects.get(id=quiz_id)
        questions = Question.objects.filter(quiz=quiz)
        count = Question.objects.filter(quiz=quiz).count()
        if number > count:
            answ = Answers.objects.filter(id=idenef)[0]
            correct = answ.correct
            incorrect = answ.incorrect
            correct_pr = round(correct/count*100, 1)
            incorrect_pr = round(incorrect / count * 100, 1)
            return render(request, 'result.html', context={
                'correct': correct, 'incorrect': incorrect, 'quiz_id': quiz_id,
                'quiz': quiz, 'count': count, 'correct_pr': correct_pr, 'incorrect_pr': incorrect_pr,
            })
        else:
            question = questions[number - 1]
            return render(request, 'question.html', context={
                'question': question, 'number': number, 'quiz_id': quiz_id,
                'quiz': quiz, 'count': count, 'idenef': idenef
            })

    def post(self, request, quiz_id, number, idenef):
        flag = False
        quiz = Quiz.objects.get(id=quiz_id)
        questions = Question.objects.filter(quiz=quiz)
        question = questions[number - 1]
        count = Question.objects.filter(quiz=quiz).count()
        if request.POST.get('answers'):
            answ = Answers.objects.filter(id=idenef)[0]
            for i in request.POST.get('answers'):
                if i not in question.correct:
                    flag = True
                    break
            if flag:
                answ.incorrect = answ.incorrect + 1
            else:
                answ.correct = answ.correct + 1
            answ.save()

            return HttpResponseRedirect('/quiz/{}/question/{}/{}/'.format(quiz_id, number+1, idenef))
        else:
            return render(request, 'question.html', context={
                'question': question, 'number': number, 'quiz_id': quiz_id,
                'quiz': quiz, 'count': count, 'idenef': idenef
            })
