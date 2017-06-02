# Functions for running an encryption or decryption algorithm

ENCRYPT = 'e'
DECRYPT = 'd'

# Write your functions after this comment.  Do not change the statements above
# this comment.  Do not use import, open, input or print statements in the 
# code that you submit.  Do not use break or continue statements.

def clean_message(message):
    """ (str) -> str
    
    The function returns a copy of the message including only its alphabetical
    characters converted to uppercase.
    
    >>> clean_message('My mom is the best!')
    'MYMOMISTHEBEST'
    >>> clean_message('123goodbye')
    'GOODBYE'
    """
    
    new_message = ''
    for char in message:
        if char.isalpha():
            new_message = new_message + char.upper()
    return new_message


def encrypt_letter(letter, keystr_value):
    """ (str, int) -> str
    
    The function encrypt the given letter applying the given keystream value.
    
    >>> encrypt_letter('L', 12)
    'X'
    >>> encrypt_letter('A', 8)
    'I'
    """
    
    letter_value = ord(letter) - 65
    if (letter_value + keystr_value) > 25:
        new_value = (letter_value + keystr_value) + 65 - 26
        encrypted_letter = chr(new_value)
    else:
        new_value = letter_value + keystr_value + 65
        encrypted_letter = chr(new_value)
    return encrypted_letter

    
def decrypt_letter(letter, keystr_value):
    """ (str, int) -> str
    
    The function decrypt the given letter applying the given keystream value.
    
    >>> decrypt_letter('X', 12)
    'L'
    >>> decrypt_letter('I', 8)
    'A'
    """
    
    letter_value = ord(letter) - 65
    if (letter_value - keystr_value) < 0:
        new_value = letter_value - keystr_value + 26 + 65
        decrypted_letter = chr(new_value)
    else:
        new_value = letter_value - keystr_value + 65
        decrypted_letter = chr(new_value)
    return decrypted_letter

    
def swap_cards(deck, index):
    """ (list of int, int) -> NoneType
    
    The funtion mutates the deck by swapping the card at given index with the 
    following card.
    
    >>> swap_cards([5, 8, 1, 3, 2, 4, 7, 6], 2)
    
    >>> swap_cards([5, 6, 7, 1, 3, 2, 4], 3)
    
    """
    
    if index == len(deck) - 1:
        deck[0], deck[-1] = deck[-1], deck[0]
    else:
        deck[index], deck[index + 1] = deck[index + 1], deck[index]
        
        
def get_small_joker_value(deck):
    """ (list of int) -> int
    
    The function returns the value of the small joker for the given deck.
    
    >>> get_small_joker_value([2, 4, 7, 5, 1, 3, 6])
    6
    >>> get_small_joker_value([4, 5, 2, 1, 3])
    4
    """
    
    return max(deck) - 1


def get_big_joker_value(deck):
    """ (list of int) -> int
    
    The function returns the value of the big joker for the given deck.
    
    >>> get_big_joker_value([2, 4, 7, 5, 1, 3, 6])
    7
    >>> get_big_joker_value([4, 5, 2, 1, 3])
    5
    """
    
    return max(deck)


def move_small_joker(deck):
    """ (list of int) -> NoneType
    
    The function does Step 1 of the algorithm: swaps the small joker with the
    following card.
    
    >>> move_small_joker([2, 4, 7, 5, 1, 3, 6])
    
    >>> move_small_joker([4, 5, 2, 1, 3])
    
    """
    
    small_joker_value = get_small_joker_value(deck)
    swap_cards(deck, deck.index(small_joker_value))
    

def move_big_joker(deck):
    """ (list of int) -> NoneType
        
    The function does Step 2 of the algorithm: moves the big joker two cards
    down the deck.
        
    >>> move_big_joker([2, 4, 7, 5, 1, 3, 6])
    
    >>> move_big_joker([4, 5, 2, 1, 3])
    
    """
    
    for i in range(2):
        swap_cards(deck, deck.index(max(deck)))
        
        
def triple_cut(deck):
    """ (list of int) -> NoneType
    
    The function does Step 3 of the algorythm: all the cards above the big joker
    go to the bottom of the deck, and all the cards under the small joker go to
    the top.
    
    >>> triple cut([1, 4, 5, 2, 3])
    
    >>> triple_cut([3, 4, 5, 7, 1, 6, 2])
    
    """
    
      
    big = get_big_joker_value(deck)
    small = get_small_joker_value(deck)
    if deck.index(big) < deck.index(small):
        first_j = deck.index(big) 
        second_j = deck.index(small)
    elif deck.index(small) < deck.index(big):
        first_j = deck.index(small)
        second_j = deck.index(big)
    above_first_j = deck[:first_j]
    under_second_j = deck[second_j+1:]
    middle = deck[first_j:second_j + 1]
    deck[:] = under_second_j + middle + above_first_j
        
                                                      
def insert_top_to_bottom(deck):
    """ (list of int) -> NoneType
    
    The function does the Step 4 of the algorythm: takes the value of the
    bottom card of the deck and moves that amount of cards above the bottom
    card. If the bottom card is the big joker, we use the cmall joker as the
    number of cards.
    
    >>> insert_top_to_bottom([4, 5, 2, 1, 3])
    
    >>> insert_top_to_bottom([3, 5, 4, 2, 1, 6])
    
    """
    
    number = deck[-1]
    if number != get_big_joker_value(deck):    
        middle = deck[number:-1]
        deck[:] = middle + deck[:number] + [number]
    

def get_card_at_top_index(deck):
    """ (list of int) -> int
    
    The function returns the value of the top card as an index, and returns the 
    card at that index. If the top is the big joker, use the small joker as an 
    index.
    
    >>> get_card_at_top_index([1, 7, 6, 2, 3, 4, 5])
    7
    >>> get_card_at_top_index([4, 7, 6, 3, 5, 1, 2])
    5
    """
    
    small_joker_value = get_small_joker_value(deck)
    if deck[0] == get_big_joker_value(deck):
        return deck[get_small_joker_value(deck)]
    else:
        return deck[deck[0]]
    
    
def get_next_keystream_value(deck):
    """ (list of int) -> int
    
    The funtion does the algorythm of 5 steps until a new keystream value is
    produced.
    
    >>> get_next_keystream_value([1, 4, 5, 2, 3])
    1
    >>> get_next_keystream_value([2, 5, 3, 4, 6, 1])
    3
    """
    
    sup = len(deck)
    while sup >= max(deck) - 1:
        move_small_joker(deck)
        move_big_joker(deck)
        triple_cut(deck)
        insert_top_to_bottom(deck)
        sup = get_card_at_top_index(deck)
    return sup
    

def process_messages(deck, messages_list, encrypt_or_decrypt):
    """ (list of int, list of str, str) -> list of str
    
    The function return a list of encrypted or decrupted messages in the order
    as they are in the given list. 
    
    >>> process_messages([2, 3, 4, 1, 5, 7, 6], ['MY', 'MOM'], 'e')
    ['NA', 'RPR']
    >>> process_messages([2, 3, 4, 8, 1, 5, 7, 6], ['MY', 'MOM', 'ROCKS'], 'e')
    ['OE', 'NUO', 'VTDMX']
    """
    
    list_message = []
    for message in messages_list:
        new_message = ''
        message = clean_message(message)
        for char in message:
            if encrypt_or_decrypt == 'e':
                key_str = get_next_keystream_value(deck)
                new_message = new_message + encrypt_letter(char, key_str)
            else:
                key_str = get_next_keystream_value(deck)
                new_message = new_message + decrypt_letter(char, key_str)
        list_message.append(new_message)
    return list_message
            
    
def read_messages(given_file):
    """ (file open for reading) -> list of str
    
    The function returns a list of messages from the already open for reading
    file.
    """
    
    message_list = given_file.readlines()
    for i in range(len(message_list)):
        message_list[i] = message_list[i].strip('\n')
    return message_list
        
        
def is_valid_deck(deck):
    """ (list of int) -> bool
    
    The function checks and returns True if the given deck is valid (i.e. 
    contains every integer from 1 up to the number of cards in the deck).
    
    >>> is_valid_deck([7, 4, 6, 3, 5, 1, 2])
    True
    >>> is_valid_deck([1, 4, 3])
    False
    """
    
    flag = True
    test_deck = []
    for i in range(1, len(deck) + 1):
        test_deck.append(i)
    for value in deck:
        if value not in test_deck:
            flag = False
    return flag

    
def read_deck(deck_file):
    """ (file open for reading) -> list of int
    
    The function returns the given deck as the list of integers.
    """
    
    new_deck = [] 
    deck = deck_file.read()
    deck_list = deck.split()
    for number in deck_list:
        new_deck.append(int(number))
    return new_deck