import datetime

from django.shortcuts import render


# Create your views here.

def show_index_page(request):
    context = {
        'value': 'Lorem ipsum dolor sit amet',
        'foods': [
            {'name': 'Apple', 'category': 'Fruit'},
            {'name': 'Banana', 'category': 'Fruit'},
            {'name': 'Corn', 'category': 'Vegetable'},
            {'name': 'Grape', 'category': 'Fruit'},
            {'name': 'Hamburger', 'category': 'Meat'},
            {'name': 'Pepper', 'category': 'Vegetable'},
        ],
        'float_value': 35.4241234,
        'some_list': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'date': datetime.datetime.now(),
        'date_to': datetime.datetime(2025, 1, 1),
        'url': 'https://www.example.org/foo?a=b&c=d',
        'phone': '1-800-WORDS',
    }
    return render(request, 'app/index.html', context=context)
