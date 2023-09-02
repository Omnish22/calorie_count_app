from django.shortcuts import render, redirect
from .models import Food, Consume


# Create your views here.
def index(request):
    if request.method == 'POST':
        food_consumed_name = request.POST.get('food_consumed')
        food_consumed_object = Food.objects.get(name=food_consumed_name)

        # GET CURRENT USER 
        user = request.user 

        consume = Consume(user=user, food_consumed=food_consumed_object)
        consume.save()


    foods = Food.objects.all()
    user_consumed_food = Consume.objects.filter(user=request.user)
    return render(request, "app/index.html", {"foods":foods, "user_consumed_food":user_consumed_food})


def remove(request,id):
    consume_object = Consume.objects.get(id=id)
    if consume_object:
        consume_object.delete()
    return redirect("/")
