print("Number guessing game") 
name=input("Enter your name :")
print(f"Hi! 👋{name},Let's play a game of number guessing")

choice=input("Do you want to play? (yes/no): ").lower()
if choice=="yes":
    import random
    number_to_guess=random.randint(1,100)
    turn=5
    while turn>0:
        try:
            guess_num=int(input("Guess a number between 1 and 100 :"))
        except ValueError:
            print("invalid choice,please enter a valid number")
            continue
        if guess_num<number_to_guess:
              print("Too low!")
        elif guess_num>number_to_guess:
              print("Too High!")
        else:
              print(f"Well done🎉! you guessed the right number {number_to_guess}")
              break
        turn-=1     
        if turn>0:
            print(f"you have {turn} turn{'s' if turn>1 else ''} left")
            print("keep guessing")
    else:
        print("❌Game over!")
        print("you have used all your turns 😔.")
    
       
        
elif choice == "no":
    print("ok bye")
else:
    print("invalid choice")