import json

from django.http import JsonResponse
from django.shortcuts import render

from .forms import *
from .parse import get_keywords


def parser_home(request):
    context = {}
    if request.method == 'POST':
        print('request.POST', request.POST)
        print('request.POST', request.POST['url'])

        url = request.POST['url']
        scholarship = get_keywords(url)
        response_data = {
            'url': request.POST['url'],
            'status': 'success',
            'scholarship': scholarship,
            'metadata': {},
        }

        if 'title' in scholarship:
            context['title'] = scholarship['title']

        context['response_data'] = json.dumps(response_data, indent=2)

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

        return JsonResponse(response_data, json_dumps_params={'indent': 2, 'sort_keys': True})
    except KeyError:
        return JsonResponse({"error": "Please pass a URL"})
