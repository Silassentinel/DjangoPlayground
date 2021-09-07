from django.http.response import Http404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

# import the models
from .models import Question, Choice

# Get Questions and display them
def index(request):
    # get a list of questions ordered descending by date per 5
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # pass the list to the template
    context = {'latest_question_list': latest_question_list}
    # render the template
    return render(request, 'polls/index.html',context)

# show a specific question and its choices
def detail(request, question_id):
    try:
        # get the question
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    # return the question
    return render(request, 'polls/detail.html', {'question': question})

# Get question and display results
def results(request, question_id):
    # check db for question or return a 404
    # pk = is via the url parameter
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# vote for a question
def vote(request, question_id):
    # get the question
    question = get_object_or_404(Question, pk=question_id)
    # get the choice
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))