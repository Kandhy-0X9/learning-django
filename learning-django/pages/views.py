
from django.shortcuts import render
from .forms import GreetingForm


def home(request):
    greeting = ""

    if request.method == "POST":
        form = GreetingForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            greeting = f"Hello, {name}!"

    else:
        form = GreetingForm()

    context = {
        "form": form,
        "greeting": greeting,
    }

    return render(request, "pages/home.html", context)
