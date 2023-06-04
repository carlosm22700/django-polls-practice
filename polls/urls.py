# to call a view, it needs to be mapped to a URL, we need URLconf for this.
from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    # ex: /polls/
    path("", views.index, name='index'),
    # ex: /polls/5/
    # added specifics
    path("specifics/<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),

]
