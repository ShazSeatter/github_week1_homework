first_name = input("What is your name?")
current_year = 2023
birth_year = input("What year were you born?")

def introduction(name, year, birth):
    print("Hello " + name + ". You are " + str(year - int(birth)) + " years old.")

introduction(first_name, current_year, birth_year)


budget = 100 
gorcery_total = 60.5

def shopping_trip(total, amount):
    if total < amount:
        print("Your total cost is " + str(total) + ". You have enough in the budget for your gorceries! :D")
    else: 
        print("You don't have enough in the budget to afford your gorceries! :(")

shopping_trip(gorcery_total, budget)








