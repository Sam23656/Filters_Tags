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
        ]
    }
    return render(request, 'app/index.html', context=context)
