from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import PizzaModel, Toppings, Sizes
from .forms import PizzaModelForm

# Create your views here.

def index(request):
    pizza = PizzaModel.objects.all().exists()
    print(pizza is False)
    return render(request, 'index.html', {'pizza': pizza})

def create(request):
    sizes = Sizes.objects.all()
    s = []
    for x in sizes:
        s.append(x.size)
    toppings = Toppings.objects.all()
    t = []
    for x in toppings:
        t.append(x.topp)
    if request.method == "POST":
        toppings = []
        for x in t:
            if request.POST.get(x) is not None:
                toppings.append(x)
        pizza = PizzaModel.objects.create(type_of_pizza = request.POST.get('type_of_pizza'), size = request.POST.get('size'), toppings = toppings)
        pizza.save()
        return redirect('index')
    else:
        return render(request, 'create.html', {'sizes':s, 'toppings': t})

def NoPizza(request):
    return render(request, 'nopizza.html')

def AllPizza(request):
    size = 'All'
    type_of_pizza = 'All'
    sizes = Sizes.objects.all()
    s = []
    for x in sizes:
        s.append(x.size)
    if request.method == 'POST':
        size = request.POST.get('size')
        type_of_pizza = request.POST.get('type')

    if size == 'All' and type_of_pizza == 'All':
        pizza = PizzaModel.objects.all()
    elif size != 'All':
        pizza = PizzaModel.objects.filter(size__contains = size)
        if type_of_pizza != 'All':
            pizza = pizza.filter(type_of_pizza__contains = type_of_pizza)
    elif type_of_pizza != 'All':
        pizza = PizzaModel.objects.filter(type_of_pizza__contains = type_of_pizza)
    
    return render(request, 'allpizza.html', {'pizza': pizza, 'sizes': s})


def Delete(request, pk):
    pizza = get_object_or_404(PizzaModel, pk = pk)

    if request.method == "POST":
        print(request.POST.get('value'))
        if request.POST.get('value')=='Yes':
            pizza = PizzaModel.objects.get(pk = pk)
            print(pizza.toppings)
            pizza.delete()
        return redirect('AllPizza')
        
    return render(request, 'delete.html')


def Edit(request, pk):
    pizza = get_object_or_404(PizzaModel, pk = pk)

    sizes = Sizes.objects.all()
    s = []
    for x in sizes:
        s.append(x.size)

    toppings = Toppings.objects.all()
    t = []
    for x in toppings:
        t.append(x.topp)

    if request.method == "POST":
        toppings = []
        for x in t:
            if request.POST.get(x) is not None:
                toppings.append(x)
        pizza = PizzaModel.objects.get(pk = pk)
        pizza.size = request.POST.get('size')
        pizza.type_of_pizza = request.POST.get('type_of_pizza')
        pizza.toppings = toppings
        pizza.save()
        return redirect('AllPizza')
    else:
        form = PizzaModelForm()
    return render(request, 'create.html', {'sizes':s, 'toppings': t})

def Layout(request):
    if request.method == 'POST':
        if request.POST.get('size')!='':
            size_model = Sizes(size = request.POST.get('size').capitalize())
            size_model.save()

        if request.POST.get('toppings')!='': 
            toppings_model = Toppings(topp = request.POST.get('toppings').capitalize())
            toppings_model.save()
        return redirect('index')
    else:
        return render(request, 'layout.html')



