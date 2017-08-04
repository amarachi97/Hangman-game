from draw_hangman import draw_hangman 
def game_processor(word):
    spaces = "-" * len(word)
    print("_ "*len(word))
    error = 0
    while ('-' in spaces) and (error <= 6):
        guess = input("enter your guess: ")
        if guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("invalid input")
            continue
        else:
            if guess in word:
                for idx in range(0,len(word)):
                    if word[idx] == guess:
                        if guess == spaces[idx]: #if the letter has already been entered
                            continue
                        else:
                            spaces = spaces[0:idx] + guess + spaces[idx+1:] #concatenating the result
                            print(draw_hangman(error))
                            print(spaces)
                            break
                    else:
                        continue
            else:
                error += 1
                if error == 6:
                    print("WHOOPS!! 6 errors")
                    print("YOU LOST")
                    print()
                    print("the word was:")
                    return word
                    break
                else:
                    print(draw_hangman(error))
                    print(spaces)
    return ' '

