# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, cash_value):
    pet_shop["admin"]["total_cash"] += cash_value


def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, number_of_pets_sold):
    pet_shop["admin"]["pets_sold"] += number_of_pets_sold


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])


def get_pets_by_breed(pet_shop, target_breed):
    pets_of_target_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == target_breed:
            pets_of_target_breed.append(pet)
    return pets_of_target_breed


def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet
    return None



def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)


def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)


def get_customer_cash(customer):
    return customer["cash"]


def remove_customer_cash(customer, cash_to_remove):
    customer["cash"] -= cash_to_remove


def get_customer_pet_count(customer):
    return len(customer["pets"])


def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)


def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    else:
        return False

    
def sell_pet_to_customer(pet_shop, pet_being_sold, customer):

    if pet_being_sold != None:
        cost_of_pet = pet_being_sold["price"]
        name_of_sold_pet = pet_being_sold["name"]
        print(f"pet {name_of_sold_pet} found")

        if customer_can_afford_pet(customer, pet_being_sold):
            print("customer can afford pet")
            print("selling pet to customer")
            remove_customer_cash(customer, cost_of_pet)
            add_or_remove_cash(pet_shop, cost_of_pet)
            remove_pet_by_name(pet_shop, name_of_sold_pet)
            increase_pets_sold(pet_shop, 1)
            add_pet_to_customer(customer, pet_being_sold)
        else:
            print("Error: customer cannot afford pet")
    else:
        print("Error: pet not found")