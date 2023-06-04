from django.http import HttpResponse
# from django.http import Http404
from django.shortcuts import get_object_or_404, render
# from django.template import loader

from .models import Question

# Create your views here.
# this would be like the controller in an MVC app


# def index(request): this uses the loader import
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("polls/index.html")
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

# using render():
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    # render() takes the request obj as its first arg, a template name as the second, and a dictionary as its optional third argument. It returns an HttpResponse obj of the given template rendered with the given context
    return render(request, "polls/index.html", context)


# def details(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, "polls/details.html", {"question": question})

# shortcut using the get_object_or_404() import

def detail(request, question_id):
    # get_object_or_404() function takes a Django model as its first argument and an arbitrary number of keyword arguments, which it passes to the get() function of the model's manager. It rasies Http404 if obj doesnt exist
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/details.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
