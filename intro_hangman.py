#Author: AMARACHI IWUH

print("******THE HANGMAN!!!!********")
print("Instructions:")
print("1. For the default mode, a hardcoded word will be used to generate the empty spaces.")
print("2. For the human against human game, a user will type in a random word, the computer will hide it and the opponent will try and figure it out")
print("3. For the human against computer game, the most difficult of all, the computer prints dashes to hide the mystery word and the user is made to figure the word out")
print("If a letter is repeated and the word has no duplicate of the letter, the user will be asked for a new guess")
print("These challenges are only for the FEARLESS!")
print("*the guesser has only 6 guesses. Use wisely")

print("For the default mode, press 1")
print("For the human against human game, press 2")
print("For the human against computer game, press 3")
print()

while True:
    decision = int(input("enter decision: "))
    if decision == 1:
        print()
        from first_mode import first_mode
        print(first_mode())
        break
    
    elif decision == 2:
        print()
        from human_human_games import human_human_games
        print(human_human_games())
        break
    
    elif decision == 3:
        print()
        from third_mode import third_mode
        print(third_mode())
        break
    
    else:
        continue
    

