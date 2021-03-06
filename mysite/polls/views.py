from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

def index(request):
    return HttpResponse("Hello,world. You're at the polls index")

def detail(request, question_id):
    try:
        question = Question.objects.get(pk= question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    #request.POST['choice'] will raise KeyError if choice wasn’t provided in POST data.
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk= question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))
#Always return an HttpResponseRedirect after successfully dealing
# with POST data. This prevents data from being posted twice if a user hits the Back button.
#the code returns an HttpResponseRedirect rather than a normal HttpResponse: post쓸 때는 normal http말고 redirect써야 안전



