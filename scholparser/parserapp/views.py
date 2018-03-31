from .forms import *
from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def parser_home(request):
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

    return render(request, "parserapp/parser.html", context)

def parse(request):
    try:
        parse_url = request.GET['url']
        return JsonResponse({"Success": "This has been parsed"})
    except KeyError:
        return JsonResponse({"error": "Please pass a URL"})


