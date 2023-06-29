import random
# Picking up a Rondom Number
x = random.randint(0,9)

# list for checking valid input
valid = ['g','r','v','1','2','3','4','5','6','7','8','9','0']

# Functions for printing Message of win or loose
def congrats(y):
    print(f"Congrats you have Won {y}Rupees")

def sorry():
    print("Sorry Better Luck Next Time!")

def color (x):
    if x == 1 or x == 3 or x == 7 or x == 9:
        print(f"The Color is Green and the Number was {x}")
    elif x == 0 or x == 5:
        print(f"The color was voilate and the Number was {x}")
    else:
        print(f"The color was Red and the Number was {x}")

# Taking input from the user

print("press g for Green")
print("press r for red")
print("press v for voilate")
print("Winning Amounts\nFor valid Green or Red prediction 1:2\nFor valid Voilate prediction 1:3\nFor valid Number Prediction 1:9")
print("Do you want to Bet on Green/Red/Voilate/Number")
y = input("On which you want to bet: ")

# Checking the condition according the user input and telling weather he won or lost
if y not in valid:
    raise ValueError("Please Enter a Valid color or Number")
elif y =='g':
    if x==1 or x==3 or x==7 or x==9:
        congrats(20)
    else:
        sorry()
elif y == 'v':
    if x == 0 or x == 5:
        congrats(35)
    else:
        sorry()
elif y == 'r':
    if x == 2 or x == 4 or x == 6 or x == 8:
        congrats(20)
    else:
        sorry()
else:
    if x == 1 or x == 3 or x == 7 or x == 9:
        if x == int(y):
            congrats(90)
        else:
            sorry()
    elif x == 0 or x == 5:
        if x == int(y):
            congrats(90)
        else:
            sorry()
    else:
        if x == int(y):
            congrats(90)
        else:
            sorry()
                    
color(x)








