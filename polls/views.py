from django.http import HttpResponseRedirect
# from django.http import Http404
from django.shortcuts import get_object_or_404, render
# from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

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
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {"latest_question_list": latest_question_list}
#     # render() takes the request obj as its first arg, a template name as the second, and a dictionary as its optional third argument. It returns an HttpResponse obj of the given template rendered with the given context
#     return render(request, "polls/index.html", context)


# # def details(request, question_id):
# #     try:
# #         question = Question.objects.get(pk=question_id)
# #     except Question.DoesNotExist:
# #         raise Http404("Question does not exist")
# #     return render(request, "polls/details.html", {"question": question})

# # shortcut using the get_object_or_404() import

# def detail(request, question_id):
#     # get_object_or_404() function takes a Django model as its first argument and an arbitrary number of keyword arguments, which it passes to the get() function of the model's manager. It rasies Http404 if obj doesnt exist
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing with POST Date.
        # This prevents data from being posted twice if a user hits the Back button
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

    # request.POST is a dictionary-like object that lets you access submitted date by key name. In this case, request.POST['choice'] returns the ID of the selected choce, as a string. request.POST values are always strings.

    # request.POST['choice'] will raise KeyError if choice wasn't provided in POST data. The above code check for KeyError and redisplays the question form with an error message if choice isn't given

    # After incrementing the choice count, the code returns an HttpResponseRedirect rathen than a normal HttpResponse. HttpResponseRedirect takes a single argument: the URL to which the user will be redirected.

    # We are using the reverse() function in the HttpResponseRedirect constructor in this example. This function helps avoid having to hardcode a URL in the view function. It is given the name of the view that we want to pass control to and the variable portion of the URL pattern that points to that view. In this case, using URLconf we set up earlier. Itll return a string like "/polls/3/results/"
