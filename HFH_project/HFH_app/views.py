from django.shortcuts import render
from . import models
from django.shortcuts import redirect


# Create your views here.
def main(request):
    return render(request, 'home_page/index.html')


def about_us(request):
    return render(request, "info-pages/about-us.html")


def contact_us(request):
    return render(request, "info-pages/contact_us.html")


def help(request):
    return render(request, "info-pages/help.html")


def calorie_counter(request):
    # get all foods from our database
    retrieved_food_items = models.Food.objects.all()
    # get all eaten foods from database
    retrieved_eaten_foods = models.FoodsEatenList.objects.get(id=1)
    total_calories = 0
    for food in retrieved_eaten_foods.foodEaten.all():
        print(food.calories)
        total_calories += food.calories
    print(total_calories)
    return render(request, "feature_pages/calorie-counter.html", {'food_items': retrieved_food_items, 'foods_eaten': retrieved_eaten_foods, 'total_calories': total_calories })


def add_eaten_food(request, food_id):
    food = models.Food.objects.get(id=food_id)
    foodAdded, created = models.FoodsEatenList.objects.get_or_create(id=1)
    foodAdded.foodEaten.add(food)
    foodAdded.save()
    print('This was the food added to list: ')
    print(foodAdded.id)
    print(foodAdded.foodEaten)
    #foodAdded.foodEaten.add(food)
    #foodAdded.save()
    print("Food item info: ")
    print(food.id)
    print(food.name)
    return redirect('calorie_counter')

def delete_eaten_food(request, food_id):
    food = models.Food.objects.get(id=food_id)
    foodRemoved = models.FoodsEatenList.objects.get(id=1)
    foodRemoved.foodEaten.remove(food)
    return redirect('calorie_counter')


def profile(request):
    return render(request, "Login_pages/profile.html")


def login(request):
    return render(request, 'Login_pages/login.html')


def sign_up(request):
    return render(request, 'Login_pages/sign_up.html')


def privacy_policy(request):
    return render(request, 'legal_pages/privacy_policy.html')


def terms_of_service(request):
    return render(request, 'legal_pages/terms_of_service.html')


# buttons doesn't work yet
# request to make new account
def get_started(request):
    return render(request, 'home_page/index.html')
