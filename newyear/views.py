from django.shortcuts import render
from datetime import datetime

# Create your views here.


def index(request):
    now = datetime.now()
    newyear = "no"
    if now.day == 1 and now.month == 1:
        newyear = "yes"
    else:
        newyear = "no"

    context = {
        "newyear": newyear.upper()
    }
    return render(request, "newyear/index.html", context)
