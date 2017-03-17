from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.http import HttpResponse
from .models import Question

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('app/index.html')
	data = {'latest_question_list': latest_question_list,}
	return HttpResponse(template.render(data, request))

def detail(request, question_id):
	return HttpResponse("you are looking at question %s." %question_id)

def result(request, question_id):
	return HttpResponse("you are looking at the result of question %s." %question_id)

def vote(request, question_id):
	return HttpResponse("you are voting on question %s." %question_id)