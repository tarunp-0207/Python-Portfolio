import random
secret_no=random.randint(1,10)
attempts=3

print("I'm thinking a number between 1 and 10")

while attempts>0:
    guess=int(input("take a guess:"))
    if guess==secret_no:
        print("congratulations ! you guessed the number!")
        break
    elif guess<secret_no:
        print("too low!try again")
    else:
        print("too high!try again")
    attempts-=1

if attempts==0:
    print("sorry , you've run out of attempts.the secret number was :",secret_no)
        
    
