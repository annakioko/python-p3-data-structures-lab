spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [dish['name'] for dish in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return[spicy for spicy in spicy_foods if spicy.get('heat_level',0) >5]

def print_spicy_foods(spicy_foods):
     for foods in spicy_foods:
        heat_level = '🌶' * foods.get('heat_level', 0) 
        print(f"{foods['name']} ({foods['cuisine']}) | Heat Level: {heat_level}")
   

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for foods in spicy_foods:
       if foods.get('cuisine') == cuisine:
        return foods
       
      

def print_spiciest_foods(spicy_foods):
     for spicy in spicy_foods:
        heat_level = '🌶' * spicy.get('heat_level', 0)  
        if spicy.get('heat_level', 0) > 5:
            print(f"{spicy['name']} ({spicy['cuisine']}) | Heat Level: {heat_level}")


def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food.get('heat_level', 0) for food in spicy_foods)
    i_spicy_foods = len(spicy_foods)
    if i_spicy_foods == 0:
        return 0
    return total_heat_level // i_spicy_foods

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

#come back and check why my emoji code was bring an error