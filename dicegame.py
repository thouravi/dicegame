import random
result = random.randint(1,100)

amount = int(input("Enter the amount to bet:"))
chance = int(input("Select the multiplier of winning:"))

if chance == 1:
    win = 100
elif chance == 2:
    win = 50
elif chance == 3:
    win = 33
elif chance == 4:
    win = 12
else:
    print ("Maximum multiplier value is 4!")
    exit()

prize = amount * chance

print ("Your base amount is $" + str(amount) + " and If you win, you will get $" + str(prize) + ".")
print ("You will only win if your number is less than or equals to " + str(win) + ".")


if result <= win:
    print ("You won $" + str(prize) + "! The number is " + str(result))
else:
    print ("You lost $" + str(prize) + "! The number is " + str(result))