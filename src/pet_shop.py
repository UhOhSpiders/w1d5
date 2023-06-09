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
        
def remove_pet_by_name(pet_shop, pet_name):
  pet = find_pet_by_name(pet_shop, pet_name)
  pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash_int):
    customer["cash"] -= cash_int

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

# optional

def customer_can_afford_pet (customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    else:
        return False

def sell_pet_to_customer (pet_shop, pet, customer):
    if pet not in pet_shop["pets"]:
        return None
    if customer["cash"] < pet["price"]:
        return None
    customer["cash"] -= pet["price"]
    pet_shop["admin"]["total_cash"] += pet["price"]
    customer["pets"].append(pet)
    pet_shop["admin"]["pets_sold"] += len(customer["pets"])




