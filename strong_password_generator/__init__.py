from random import *
from time import *
the_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
the_number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
the_symbol = ['`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '~', '/', '-', '+', ';', '?', '.', ',', '<', '>', ':', '"', '[', ']', ']', '{', '}', '_', '=']
the_word_match_set = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '~', '/', '-', '+', ';', '?', '.', ',', '<', '>', ':', '"', '[', ']', ']', '{', '}', '_', '=']
the_random_character_array = [the_word_match_set[randint(0, 90)], the_word_match_set[randint(0, 90)], the_word_match_set[randint(0, 90)], the_word_match_set[randint(0, 90)], the_word_match_set[randint(0, 90)], the_word_match_set[randint(0, 90)], the_word_match_set[randint(0, 90)], the_word_match_set[randint(0, 90)], the_word_match_set[randint(0, 90)]]


# 生成强密码
def generate_a_strong_password():
    password = ''
    clock = strftime("%S")
    if len(clock) == 1:
        clock = str(clock) + str(randint(0, 9))
    print(int(list(clock)[randint(0, 1)]))
    password = password + the_random_character_array[int(list(clock)[randint(0, 1)])]
    password = the_letter[randint(0, 25)]
    password = password + the_symbol[randint(0, 29)]
    for i in range(3):
        password = password + the_number[randint(0, 9)]
    password = password + the_random_character_array[int(list(clock)[randint(0, 1)])]
    for i in range(2):
        password = password + the_letter[randint(0, 25)]
    password = password + the_symbol[randint(0, 29)]
    for i in range(2):
        password = password + the_random_character_array[int(list(clock)[randint(0, 1)])]
    for i in range(4):
        password = password + the_symbol[randint(0, 29)]
    password = password + the_number[randint(0, 9)]
    return password
