from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "name": "Kandhy",
        "topic": "Django",
    }

    return render(request, "pages/home.html", context)