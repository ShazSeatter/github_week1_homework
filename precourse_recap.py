first_name = "Shaz"
current_year = 2023
birth_year = 1996

def introduction(name, year, birth):
    print("Hello " + name + ". You are " + str(year - birth) + " years old.")

introduction(first_name, current_year, birth_year)


budget = 100 
gorcery_total = 60.5

def shopping_trip(total, amount):
    if total < amount:
        print("Your total cost is " + str(total) + ". You have enough in the budget for your gorceries! :D")


shopping_trip(gorcery_total, budget)








