from .forms import *
from django.shortcuts import render


# Create your views here.
def parser(request):
    if request.method == 'POST':
        parser_form = ParserForm(request.POST)

        if parser_form.is_valid():
            print('valid')
        else:
            print('invalid')

    else:
        parser_form = ParserForm(request.POST or None)
        context = {
            "parser_form": parser_form,
        }

    return render(request, "parser.html", context)
