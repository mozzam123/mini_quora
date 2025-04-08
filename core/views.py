from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from .forms import UserRegistrationForm, QuestionForm, AnswerForm
from .models import Question, Answer
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def logout_user(request):
    logout(request)
    return redirect('login')
     

def signup_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now login.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'core/signup.html', {'form': form})

@login_required
def post_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            messages.success(request, 'Question posted successfully!')
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request, 'core/post_question.html', {'form': form})


def home(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'core/home.html', {'questions': questions})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST' and request.user.is_authenticated:
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            messages.success(request, 'Answer posted successfully!')
            return redirect('question_detail', pk=question.pk)
    else:
        form = AnswerForm()
    return render(request, 'core/question_detail.html', {'question': question, 'form': form})

@login_required
def like_answer(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    if request.user in answer.likes.all():
        answer.likes.remove(request.user)
        messages.info(request, 'You unliked the answer.')
    else:
        answer.likes.add(request.user)
        messages.success(request, 'You liked the answer!')
    return redirect('question_detail', pk=answer.question.pk)
