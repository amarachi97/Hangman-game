#Author: AMARACHI IWUH

from random import randint
from game_processor import game_processor
def third_mode():
    open_file = open('word_list.txt', 'r')
    lines = open_file.readlines()
    while True:
        comp_word = randint(0, 5014)
        word = lines[comp_word]
        word = word.strip()
        if len(word) >= 5:
            result = game_processor(word)
            return result
        
        else:
            continue
    open_file.close()
    
