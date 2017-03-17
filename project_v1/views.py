from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Question
from django.http import Http404

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	data = {'latest_question_list': latest_question_list,}
	return render(request,'app/index.html', data)

def detail(request, question_id):
	try:
		question = Question.objects.get(pk = question_id)
	except Question.DoesNotExist:
		raise Http404("the Question you are looking for does not exist")
	data = {'question' : question}
	return render(request, "app/detail.html", data)

def result(request, question_id):
	return render(request, "you are looking at the result of question %s." %question_id)

def vote(request, question_id):
	return render(request, "you are voting on question %s." %question_id)