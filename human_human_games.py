#Author: AMARACHI IWUH
from game_processor import game_processor
def human_human_games():
    word = input("provide a word for your opponent: ")
    for empty_space in range(0,101):
        print(' ')
    result = game_processor(word)
    return result
    
