from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Choice, Question
from django.conf.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	data = {'latest_question_list': latest_question_list,}
	return render(request,'project_v1/index.html', data)

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	data = {'question' : question}
	return render(request, "project_v1/detail.html", data)

def result(request, question_id):
	return render(request, "you are looking at the result of question %s." %question_id)

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except(KeyError, Choice.DoesNotExist):
		return render(request, 'project_v1/detail.html',{
			'question': question,
			'error_message': "You didn't select a choice",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
	return HttpResponseRedirect(reverse('project_v1:results', args=(question.id,)))