import random

print(' welcome to number guessing game')
print(' Enter number between 1 to 20')
a = random.randint(1, 20)
for i in range(6):
    print('Enter your '+ str(i + 1) + ' guessing value :')
    guess = input()
    if int(guess) >a:
        print('is smaller then : ' + guess)
    elif int(guess) <a:
        print('is grater then :' +guess)
    else:
        break
if int(guess) ==a:
    print('you win,  you guest it in ' + str(i+1) + ' times')
print('thanks for playing the game')
