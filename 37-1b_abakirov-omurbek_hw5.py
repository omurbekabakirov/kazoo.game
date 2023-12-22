import logic
from decouple import config

your_cash = int(config('MY_MONEY',default=1000))
while your_cash > 0:
    answer = input("Would you like to play ? (yes/no): ").lower()
    if answer == 'no':
        print(f"Thanks for playing!,That is your cash: {your_cash}$")
        break
    elif answer == 'yes':
        your_bet = int(input("How much money would you bet: "))
        if your_bet>your_cash or your_bet<0:
            print("Sorry,you should bet from 1$ to 1000$")
            continue
        chosen_num = int(input("What number would you like to bet on(from 1 to 30): "))
        if chosen_num > 30 or chosen_num < 1:
            print("You must enter a number between 1 and 30")
            continue
        if chosen_num == logic.win_slot:
            print("Congratulations!")
            your_cash += your_bet * 2
        else:
            print("Sorry,you lose")
            your_cash -= your_bet
    else:
        print("You must enter yes or no")