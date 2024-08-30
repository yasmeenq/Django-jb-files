from django.shortcuts import render

# Home view 

def home(request):
    context = {"active" : "home"}
    return render(request, "home.html", context )


def about(request):
    context = {"active" : "about"}
    return render(request, "about.html", context)