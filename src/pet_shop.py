# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash_int):
    pet_shop["admin"]["total_cash"] += cash_int
    return 

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, sale_int):
    pet_shop["admin"]["pets_sold"] += sale_int
    return

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed_name):
    pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed_name:
            pets.append(1)
    return pets




def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"]== pet_name:
            return pet



