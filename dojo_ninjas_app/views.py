from django.shortcuts import render, redirect
from .models import Dojo, Ninja

# Create your views here.
def index(request):


        
    context = {
        "all_ninjas": Ninja.objects.all(),
        "all_dojos": Dojo.objects.all(),
    }



    return render(request, "index.html", context)

def add_dojo(request):
    name = request.POST["name"]
    city = request.POST["city"]
    state = request.POST["state"]

    Dojo.objects.create(name=name, city=city, state=state)

    return redirect("/")

def add_ninja(request):
    dojo = request.POST["dojo"]
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]

    userdojo = Dojo.objects.get(id=dojo)

    Ninja.objects.create(dojo=userdojo, first_name=first_name, last_name=last_name)

    return redirect("/")

def delete_dojo(request, dojo_id):
    dojo = Dojo.objects.get(id=dojo_id)

    for ninja in Ninja.objects.all():
        if ninja.dojo == dojo:
            ninja.delete()
    dojo.delete()

    return redirect("/")