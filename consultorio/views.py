from django.shortcuts import render

def home_view(request):

    context = {
        "teste": "XXX",
        "range": [0]*10
    }
    return render(request, "home.html", context)