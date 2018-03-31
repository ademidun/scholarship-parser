from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import json
from .forms import *
from .parse import get_keywords


def parser_home(request):
    context = {}
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
        keywords = get_keywords(parse_url)

        response_data = {
            'scholarship': keywords,
            'url': parse_url,
            'metadata': {},
            'status': 'success'
        }

        return JsonResponse(response_data, json_dumps_params={'indent': 2,'sort_keys': True})
    except KeyError:
        return JsonResponse({"error": "Please pass a URL"})
