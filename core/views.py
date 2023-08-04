from django.shortcuts import render
from item.models import category, Item

# from django.http import HttpResponse

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold = False)
    categories = category.objects.all()
    # print(items, categories)
    return render (request, 'core/index.html', {
        'categories':categories,
        'items':items
    })


def contact(request):
    return render (request, 'core/contact.html')
