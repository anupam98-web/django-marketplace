from django.shortcuts import render, redirect
from item.models import category, Item
from .forms import SignupForm, LoginForm

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


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login')

    form = SignupForm()
    return render(request, 'core/signup.html', {'form':form})