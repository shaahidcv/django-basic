from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def print_hello(request):
    movie_data = { 'movies' :[{
        'title': 'GodFather',
        'year' : 1990,
        'summery': 'story of an underworld king',
        'sucess': True,

    },
    {
        'title': 'Titanic',
        'year' : 1980,
        'summery': 'story of ship wrack',
        'sucess': True,

    },
    {
        'title': 'Brodaddy',
        'year' : 2024,
        'summery': 'story of dad and son',
        'sucess': False,

    },
    
    ]}
    return render(request,'hello.html',movie_data)

