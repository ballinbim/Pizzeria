from django.shortcuts import render
from .models import Pizza, Topping
from .forms import CommentForm

# Create your views here.
def index(request):
    '''The home page for Pizzeria'''
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def toppings(request):
    topping = Topping.objects.order_by('date_added')
    pizzas = Topping.pizzas_set.order_by('date_added')
    context = {'toppings': toppings, 'pizzas':pizzas}
    return render(request, 'pizzas/toppings.html', context)

def comments(request):
    if request.method != 'POST':
        form = CommentForm
    else:
        form = CommentForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizzas:toppings')

    context = {'form': form}
    return render(request, 'pizzas/comments.html', context)
        