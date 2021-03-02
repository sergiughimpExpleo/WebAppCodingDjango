from django.shortcuts import render

from personal.models import Question
from django.shortcuts import render
# Create your views here.


def home_screen_view(request):
    context = {}
    # context['some_string'] = "This is some string that I'm passing to the view"
    # context['some_number'] = 425332

    # context = {
    #     'some string': "This is some string that I'm passing to the view",
    #     'some_number': 425332,
    # }

    # list_of_values = []
    # list_of_values.append("First entry")
    # list_of_values.append("Second entry")
    # list_of_values.append("Third entry")
    # list_of_values.append("Fourth entry")
    # context['list_of_values'] = list_of_values

    questions = Question.objects.all()
    context['questions'] = questions

    return render(request, "personal/home.html", context)
