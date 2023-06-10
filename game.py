#first game that i decided to make
import time
import random
import os
import sys
spin_cash = random.randint(1,500)
thirst = 0
apple = 0
banana = 0
pear = 0
hamburger = 0
cheese_sticks = 0
fries = 0
coca_cola = 0
pepsi = 0
fanta = 0
sprite = 0
hunger = 0
price_apple = 5
price_banana = 8
current_job = ''
showing_finger_up = '\U0001F446' 
showing_finger = '\U0001F447'
face_smiling = '\U0001F600'
price_house = 600
cooldown = 4
cash = 0
need_house = price_house - cash
count_house = 0
count_car = 0
count_car = 0
count_apple = 0
car = 400
need_miner = 100
need_cash_miner = need_miner - cash
need_car = car - cash
cooldown_spin = 0
inventory = (f"You have {count_house} house,{count_car} car")
a = input(">")
while True:
    if a == 'buy':
        print("Please enter something to buy")
        a = input(">")
    if a == 'price house':
        print(f"The price of the house is 600 and you have {cash} cash.")
        a = input(">")
    if a == 'buy house':
        if cash >= price_house:
            cash -= price_house
            print("The house bought succesfully.Cash after the shopping is ",cash)
            a = input(">")
        else:
            print(f"Sorry,you dont have enough money.You need {need_house} more money")
            a = input(">")
    if a == 'buy car':
        if cash >= car:
            cash -= car
            count_car += 1
            print("Succesfully bought, the cash after shopping is ",cash)
            a = input(">")
    if a == 'buy car':
        if car > cash:
            print(f'Sorry you cant buy it.You need {need_car} more cash')
            a = input(">")
    if a == 'cash':
        print("Your cash is ",cash)
        a = input(">")
    if a == 'count car':
        print(f"You have {count_car} cars in garage")
        a = input(">")
    if a == 'price car':
        print("The price of car is ",car)
        a = input(">")
    if a == 'job list':
        print("The current jobs are \n")
        print("Waiter(waitress) --> 10 cash per works and its free(type apply waiter for apply)\n")
        print("Miner --> 50 cash per work(costs 100 cash)\n")
        print("Constructor --> 60 cash per work (costs 200 cash)\n")
        print("Librarian --> 100 cash per work (costs 500 cash)\n")
        a = input(">")
    if a == 'apply waiter':
        current_job = 'waiter'
        print("You applied as waiter,type work waiter for work")
        a = input(">")
    if a == 'work waiter':
        if current_job != 'waiter':
            print("First apply to this job")
            a = input(">")
        else:
            print("You are working now..")
            time.sleep(cooldown)
            cooldown += 3
            cash += 10
            print("You get 10 cash")
            a = input(">")
    if a == 'apply miner':
        if cash >= 100:
            cash -= 100
            print("You applied as miner")
            current_job = 'miner'
    if a == 'apply miner':
        if cash < 100:
            print(f"You dont have enough money.For apply as miner you need {need_cash_miner} cash")
            a = input(">")
    if a == 'work miner':
        if current_job == 'miner':
            print("Mining..")
            time.sleep(cooldown)
            cooldown += 4
            cash += 50
            print("Mining ended ")
            a = input(">")
        else:
            print("First apply to this job")
            a = input(">")
    if a == 'current job':
        print(f"Your current job is {current_job}")
        a = input(">")
    if a == 'help':
        print(f"The guide of the game {showing_finger}{showing_finger}{showing_finger} \n")
        print("For know the jobs  -- job list \n")
        print("For know the price of anything -- price <something> \n")
        print("For apply a job -- apply <job name> \n")
        print("For buy anything -- buy <name of the thing> \n")
        print("For know your cash -- cash \n")
        print("For know your job -- current job\n")
        print("For go to the mall -- mall shopping\n")
        print("For spinning a wheel and take any cash between 1,500 -- spin\n")
        print("For get your hunger information -- hunger\n")
        print("For delete messages -- clear\n")
        print("")
        print(f"Keep entertaining {face_smiling}")
        a = input(">")
    if a == 'apply constructor':
        if cash >= 200:
            cash -= 200
            current_job = 'constructor'
            print("You applied as constructor.")
            a = input(">")
    if a == 'apply constructor':
        if cash < 200:
            print("Sorry you cant work as constructor")
            a = input(">")
    if a == 'work constructor':
        if current_job == 'constructor':
            print("You are working now..")
            time.sleep(cooldown)
            cooldown += 3
            cash += 60
            a = input(">")
        else:
            print("First apply to this job")
            a = input(">")
    time.sleep(10)
    hunger += 2
    if a == 'hunger':
        print(f"Your hunger is {hunger}")
        a = input(">")
    if a == 'count sprite':
        print(f"You have {sprite} sprite")
        a = input(">")
    if a == 'count cola':
        print(f"You have {coca_cola} Coca_Cola")
        a = input(">")
    if a == 'count fanta':
        print(f"You have {fanta} fanta")
        a = input(">")
    if a == 'count hamburger':
        print(f"You have {hamburger} hamburger")
        a = input(">")
    if a == 'count apple':
        print(f"You have {apple} apple")
        a = input(">")
    if a == 'count banana':
        print(f"You have {banana} banana")
        a = input(">")
    if a == 'price apple':
        print("The price of the apple is 5")
        a = input(">")
    if a == 'price banana':
        print("The price of the banana is 8")
        a = input(">")
    if a == 'buy apple':
        if cash >= price_apple:
            cash -= 5
            apple += 1
            print(f"You bought an apple.You have {apple} apple")
            a = input(">")
        else:
            print("You don't have enough money")
            a = input(">")
    if a == 'buy banana':
        if cash >= price_banana:
            cash -= 8
            banana += 1
            print(f"You bought banana.You have {banana} banana")
            a = input(">")
        else:
            print("You don't have enough money")
            a = input(">")
    if a == 'count banana':
        print(f"You have {banana} banana")
        a = input(">")
    if a == 'count apple':
        print(f"You have {apple} apple")
        a = input(">")
    if a == 'stop game':
        print("Exit was succesfull")
        break
    if a == 'spin':
        cooldown_spin += 100
        print(f"You win {spin_cash} cash!")
        cash += spin_cash
        a = input(">")
    if a == 'inventory':
        print(inventory)
        a = input(">")
    if a == 'clear':
        delete_message = int(input("Enter the number of messages to delete : "))
        if delete_message:
            for i in range(delete_message):
             os.system('cls' if os.name == 'nt' else clear)
            print(f"{delete_message} messages deleted succesfully")
            a = input(">")
