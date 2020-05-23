from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'MyApp/home.html')


def about(request):
    return render(request, 'MyApp/about.html')


def contact(request):
    return render(request, 'MyApp/contact.html')


def news(request):
    return render(request, 'MyApp/news.html')


def data(request):
    my_variable = "Hello World !"
    years_old = 15
    array_city_capitale = ["Paris", "London", "Washington"]
    return render(request, 'MyApp/index.html',{"my_var": my_variable, "years": years_old, "array_city": array_city_capitale})
